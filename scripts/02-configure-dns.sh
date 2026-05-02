#!/usr/bin/env bash
set -euo pipefail

MINIKUBE_IP="$(minikube ip)"

echo "===== IP DE MINIKUBE ====="
echo "$MINIKUBE_IP"

echo ""
echo "===== LIMPIANDO ENTRADAS ANTERIORES ====="
sudo sed -i '/app.andres-lopez.com/d' /etc/hosts
sudo sed -i '/argo.andres-lopez.com/d' /etc/hosts

echo ""
echo "===== AGREGANDO DNS LOCAL ====="
echo "$MINIKUBE_IP app.andres-lopez.com argo.andres-lopez.com" | sudo tee -a /etc/hosts

echo ""
echo "===== VALIDANDO /etc/hosts ====="
grep -E "app.andres-lopez.com|argo.andres-lopez.com" /etc/hosts
