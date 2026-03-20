from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def mensaje():
    return "Bienvenidos a FastAPI ingenieros de sistemas"

@app.get("/{nombre}")
def mensaje(nombre: str):
    return f"Bienvenidos {nombre}"