from fastapi import FastAPI

app = FastAPI()

productos = [
    {
        "codigo" : 1,
        "nombre" : "Esfero",
        "valor" : 3500,
        "existencia" : 10
    },
    {
        "codigo" : 2,
        "nombre" : "Cuaderno",
        "valor" : 5000,
        "existencia" : 15
    },
    {
        "codigo" : 3,
        "nombre" : "Lapiz",
        "valor" : 200,
        "existencia" : 12
    }
]

@app.get('/')
def mensaje():
    return "Bienvenido a la tienda de papeleria"

@app.get('/{nombre}/{codigo}')
def mensaje2(nombre: str, codigo: int):
    return f"Bienvenido a la tienda de papeleria, {nombre}!"

@app.get('/uno')
def mensaje3(nombre: str, edad: int):
    return f"Bienvenido a la tienda de papeleria, {nombre}! Tu edad es {edad} años."

@app.get('/productos')
def obtener_productos():
    return productos