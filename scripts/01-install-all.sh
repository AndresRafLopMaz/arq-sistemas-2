#!/usr/bin/env bash
set -euo pipefail

echo "===== APLICANDO NAMESPACES ====="
kubectl apply -f k8s/namespaces.yaml

echo ""
echo "===== INSTALANDO TRAEFIK CRDs ====="
kubectl apply -f k8s/traefik/traefik-crds.yaml

echo ""
echo "===== INSTALANDO TRAEFIK ====="
kubectl apply -f k8s/traefik/traefik-rendered.yaml
kubectl -n traefik rollout status daemonset/traefik --timeout=180s

echo ""
echo "===== INSTALANDO ARGOCD ====="
kubectl apply -n argocd -f k8s/argocd/install.yaml
kubectl -n argocd rollout status deployment/argocd-server --timeout=300s

echo ""
echo "===== CONFIGURANDO ARGOCD EN MODO HTTP INTERNO ====="
kubectl apply -f k8s/argocd/argocd-cmd-params-cm.yaml
kubectl -n argocd rollout restart deployment/argocd-server
kubectl -n argocd rollout status deployment/argocd-server --timeout=300s

echo ""
echo "===== CREANDO RUTA DE ARGOCD CON TRAEFIK ====="
kubectl apply -f k8s/argocd/ingressroute.yaml

echo ""
echo "===== INSTALANDO APLICACION ASSIGNMENT-08 ====="
kubectl apply -f k8s/app/
kubectl -n assignment-08 rollout status deployment/assignment-08-app --timeout=180s

echo ""
echo "===== ESTADO FINAL ====="
kubectl get pods -A
kubectl get svc -A
kubectl get ingressroute -A
