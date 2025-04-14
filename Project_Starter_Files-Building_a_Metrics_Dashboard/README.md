**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation
### picture
 ![kubectl get pods and services](answer-img/kubectl_get_pods_services.png)
### text ouput
```
kubectl get pods
NAME                            READY   STATUS    RESTARTS   AGE
backend-app-8657b45598-knt4n    1/1     Running   0          8m18s
backend-app-8657b45598-grjlz    1/1     Running   0          8m18s
backend-app-8657b45598-wlnp7    1/1     Running   0          8m18s
frontend-app-5f9d7f7db9-8h4bl   1/1     Running   0          8m17s
frontend-app-5f9d7f7db9-bwxp9   1/1     Running   0          8m17s
frontend-app-5f9d7f7db9-gw75w   1/1     Running   0          8m17s
trial-app-7c4ddb7b97-4xjqp      1/1     Running   0          8m17s
trial-app-7c4ddb7b97-q8dzw      1/1     Running   0          8m17s
trial-app-7c4ddb7b97-lkjht      1/1     Running   0          8m17s

kubectl get services
NAME               TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
kubernetes         ClusterIP      10.43.0.1      <none>        443/TCP          37m
backend-service    LoadBalancer   10.43.196.97   10.0.2.15     8081:31852/TCP   8m40s
frontend-service   LoadBalancer   10.43.235.66   10.0.2.15     8080:32378/TCP   8m40s
trial-service      LoadBalancer   10.43.244.49   10.0.2.15     8082:31708/TCP   8m39s
```
## Setup the Jaeger and Prometheus source
Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.
### picture
 ![Grafana home](answer-img/grafana_home.png)

## Create a Basic Dashboard
Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.
### picture
 ![Grafana Prometheus Source](answer-img/Grafana_promethues_source.png)

## Describe SLO/SLI
Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.
### SLO "monthly uptime"
To measure the "monthly uptime" it is nessecary to a SLI metric that evaluates the uptime of the serives and pods.
### SLO "request response time"
To measure the "request response time" a SLI to define a threshold like 200 ms, and then identify how often in percentage this threshold is meet.

## Creating SLI metrics.

### Uptime measurement
To measure the uptime, the uptime of the services will be measured, should be above 98%

### Response Time Compliance
Here is to measure the response time following the SLO target to have 95% requests ≤ 200ms.

### Error Budget Burn Rate
We check the slo violations based on the # of requests. 500 http responses shoud be < 3%

### Pod Readiness
The time that the pods are ready for the given serives shall be above 98%.

### Request Rate
Regualar have the # of requests shown on a dashboard, there is no limit assigned with this, since this hopefully will always grow as our company will grow.

## Create a Dashboard to measure our SLIs
 ![kubectl board overview](answer-img/Grafana_overview.png)

## Tracing our Flask App

 ![Jaeger simple trace](answer-img/jaeger_simple_trace.png)

  ![Python Span for Jaeger](answer-img/Python_span_example.png)


## Jaeger in Dashboards

![PTime from Jaeger in dashboard](answer-img/TimeFromJaeger.png)

## Report Error

TROUBLE TICKET

Name: Uwe Sülter

Date: 14.04.2025

Subject: Implementation of /trace is broken 

Affected Area: Start page

Severity: high

Description:
On the start page, the integration of the trial app is broken. Whenever the endpoint for /trace is called, the system shows a 500 error. Please have a look on our dashboard: project3-dashboard. It shows clearly a high number of 500 errors in % of all responses as you can see on the "500 response %" visualisation.

## Creating SLIs and SLOs

For a 99.95% monthly uptime SLO, four essential SLIs would be:
### HTTP Success Rate
(Successful HTTP responses / Total requests) × 100
Measures the percentage of requests returning 2xx/3xx status codes. Critical for detecting service outages.
### Pod Readiness Ratio
(Ready pods / Total desired pods) × 100
Tracks availability of application instances. Kubernetes-native metric via kube_pod_status_ready.
### Error Budget Consumption Rate
(Error count / Total allowed errors) × 100
Monitors how quickly errors eat into the 0.05% allowable downtime.
### Synthetic Health Check Success
(Successful synthetic probes / Total probes) × 100
Simulates user traffic to detect silent failures.
## Building KPIs for our plan


|SLI Metric| KPI| Rationale|
|--------------|--------------|---------------|
|HTTP Success Rate|30-day rolling success percentage , 5-minute error spike alerts|Provides trend analysis while enabling rapid response to outages|
|Pod Readiness|Cluster-wide readiness %, Pod restart count per hour|Combines availability tracking with instability detection|
|Error Budget|Daily burn rate, Remaining error budget days|Visualizes compliance trajectory and risk exposure|

## Final Dashboard
 ![Grafana Project Dashboard](answer-img/Grafana_final_overview.png)