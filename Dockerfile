# ---- Build stage ----
FROM node:20-alpine AS builder
WORKDIR /app

# Copiamos lockfile para que npm ci funcione
COPY package.json package-lock.json ./
RUN npm ci

# Copiamos el resto del código
COPY app/ ./
RUN npm run build

# ---- Runtime stage ----
FROM nginx:alpine

# SPA fallback (para React Router y similares)
RUN rm -f /etc/nginx/conf.d/default.conf
COPY <<'NGINXCONF' /etc/nginx/conf.d/default.conf
server {
  listen 80;
  server_name _;
  root /usr/share/nginx/html;
  index index.html;

  location / {
    try_files $uri $uri/ /index.html;
  }
}
NGINXCONF

COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
