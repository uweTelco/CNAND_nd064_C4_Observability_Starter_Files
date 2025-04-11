#!/bin/bash
docker build -t usuelter/backend-project3:latest --push .
kubectl delete -f ../../manifests/app/backend.yaml
kubectl apply -f ../../manifests/app/backend.yaml

kubectl get pods -n project3