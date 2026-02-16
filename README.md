# Assignment 01 - Load Balancer (Nginx Round Robin)

## Diagrama de infraestructura

Cliente -> http://localhost:8080 -> Nginx Load Balancer -> (Round Robin) -> web1, web2

## Comando para ejecutar la infraestructura
```bash
docker compose up -d
```

##URL del Balanceador
```bash
http://localhost:8080/
```

##Prueba Rapida
```bash
for i in {1..10}; do curl -sI http://localhost:8080 | grep -i "^X-Backend:"; done
```
