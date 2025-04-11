#!/bin/bash
docker build -t usuelter/trial-project3:latest --push .
kubectl delete -f ../../manifests/app/trial.yaml
kubectl apply -f ../../manifests/app/trial.yaml

kubectl get pods -n project3