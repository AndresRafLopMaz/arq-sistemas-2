#!/usr/bin/env bash
set -euo pipefail

echo "===== CONSTRUYENDO IMAGEN LOCAL PARA MINIKUBE ====="
minikube image build -t assignment-08-app:1.0.0 ./assignment-04-app

echo ""
echo "===== VALIDANDO IMAGEN CREADA ====="
minikube image ls | grep assignment-08-app || true
