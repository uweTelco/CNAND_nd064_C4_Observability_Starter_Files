# Installing Jaeger in Kubernetes

To install Jaeger in a Kubernetes environment, follow these steps:

## Prerequisites

Ensure the following are ready:
- A running Kubernetes cluster (e.g., Minikube, K3s, or a cloud provider)
- Helm installed on your local machine
- Sufficient system resources for Jaeger and its components
- Cert-manager installed (required for webhook validation since Jaeger Operator v1.31)

## Install Cert-Manager

Cert-manager is required for validating Jaeger custom resources. Install it using Helm:

```bash
kubectl create namespace cert-manager
helm repo add jetstack https://charts.jetstack.io
helm repo update
helm install cert-manager jetstack/cert-manager \
--namespace cert-manager \
--version v1.10.1 \
--set installCRDs=true
```

Verify the installation:

```bash
kubectl get pods -n cert-manager
```

## Install Jaeger Operator

The Jaeger Operator simplifies deploying and managing Jaeger instances. You can install it using Helm or deployment files.

### Option 1: Using Helm

Add the Jaeger Helm chart repository:

```bash
helm repo add jaegertracing https://jaegertracing.github.io/helm-charts
helm repo update
```

Install the operator:

```bash
kubectl create namespace observability
helm install jaeger-operator jaegertracing/jaeger-operator -n observability
```

Verify the installation:

```bash
kubectl get pods -n observability
```

### Option 2: Using Deployment Files

Alternatively, you can use deployment files:

```bash
kubectl create namespace observability
kubectl apply -f https://github.com/jaegertracing/jaeger-operator/releases/download/v1.53.0/jaeger-operator.yaml -n observability

```

### Post deployment steps
Install these scripts, to have the operator role and the operator binding.

```bash
kubectl apply -f Exercise_Starter_Files/jaeger/jaeger-operator-role.yaml
kubectl apply -f Exercise_Starter_Files/jaeger/jaeger-operator-binding.yaml
```
Check the deployment:

```bash
kubectl get deployment jaeger-operator -n observability
```

## Deploy a Jaeger Instance

Create a YAML file for your Jaeger instance (e.g., `jaeger-instance.yaml`):

```yaml
apiVersion: jaegertracing.io/v1
kind: Jaeger
metadata:
  name: simplest
spec:
  strategy: allInOne # Deploys all components in a single pod (ideal for testing)
  storage:
    type: memory # In-memory storage (not suitable for production)
```

Apply the configuration:

```bash
kubectl apply -f jaeger-instance.yaml -n observability
```

Verify the instance:

```bash
kubectl get jaegers -n observability
kubectl get pods -n observability
```

## Access the Jaeger UI

Forward the query service port to access the UI locally:

```bash
kubectl port-forward service/simplest-query 16686:16686 -n observability
```

Open your browser and navigate to [http://localhost:16686](http://localhost:16686).