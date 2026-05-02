# ==============================
# Etapa 1: construcción de React/Vite
# ==============================
FROM node:20-alpine AS build

# Carpeta interna del contenedor
WORKDIR /app

# Copiamos primero los manifests para aprovechar caché de Docker
COPY package*.json ./

# Instalamos dependencias exactas desde package-lock.json
RUN npm ci

# Copiamos el resto del código fuente
COPY . .

# Generamos la versión productiva de Vite
RUN npm run build


# ==============================
# Etapa 2: servidor web Nginx
# ==============================
FROM nginx:1.27-alpine

# Copiamos el build generado por Vite al directorio público de Nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Configuración mínima para SPA:
# Si la ruta no existe físicamente, regresa a index.html
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

# Puerto HTTP interno del contenedor
EXPOSE 80
