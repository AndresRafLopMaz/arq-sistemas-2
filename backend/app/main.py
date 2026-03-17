from fastapi import FastAPI

app = FastAPI(
    title="Checklist API",
    description="API para gestionar tareas de una checklist",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Backend funcionando correctamente"}