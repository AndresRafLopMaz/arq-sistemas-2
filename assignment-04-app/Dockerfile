# -------- Stage 1: Build --------
FROM node:20-alpine AS build
WORKDIR /app

# Copiamos manifests primero para cachear deps
COPY package*.json ./
RUN npm ci

# Copiamos código y construimos
COPY . .
RUN npm run build

# -------- Stage 2: Serve (nginx) --------
FROM nginx:1.27-alpine
# Vite build genera /dist; lo servimos desde nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Config minimal para SPA (fallback a index.html)
RUN cat > /etc/nginx/conf.d/default.conf <<'NGINX'
server {
  listen 80;
  server_name _;
  root /usr/share/nginx/html;
  index index.html;

  location / {
    try_files $uri $uri/ /index.html;
  }
}
NGINX

EXPOSE 80
