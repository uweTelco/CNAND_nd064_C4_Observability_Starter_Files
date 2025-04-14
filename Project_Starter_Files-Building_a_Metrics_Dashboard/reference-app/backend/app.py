from flask import Flask, render_template, request, jsonify

import pymongo
from flask_pymongo import PyMongo
from prometheus_flask_exporter import PrometheusMetrics
from flask_opentracing import FlaskTracing
from jaeger_client import Config
from jaeger_client.metrics.prometheus import PrometheusMetricsFactory
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor


app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()
app.config["MONGO_DBNAME"] = "example-mongodb"
app.config[
    "MONGO_URI"
] = "mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb"


metrics = PrometheusMetrics(app)
metrics.info("app_info", "Application info", version="1.0.3")

mongo = PyMongo(app)

def init_tracer(service):

    config = Config(
        config={
            "sampler": {"type": "const", "param": 1},
            "logging": True,
            "reporter_batch_size": 1,
        },
        service_name=service,
        validate=True,
        metrics_factory=PrometheusMetricsFactory(service_name_label=service),
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()

tracer = init_tracer("backend")
flask_tracer = FlaskTracing(tracer, True, app)

@app.route("/")
def homepage():
    return "Hello World"


@app.route("/api")
def my_api():
    with tracer.start_span("call-api") as span:
        answer = "something"
        span.log_kv({"event": "trace it", "count": 3})
        span.set_tag("api-call", answer)
        return jsonify(repsonse=answer)


@app.route("/star", methods=["POST"])
def add_star():
    star = mongo.db.stars
    name = request.json["name"]
    distance = request.json["distance"]
    star_id = star.insert({"name": name, "distance": distance})
    new_star = star.find_one({"_id": star_id})
    output = {"name": new_star["name"], "distance": new_star["distance"]}
    return jsonify({"result": output})


if __name__ == "__main__":
    app.run()
