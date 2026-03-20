from fastapi import FastAPI, Body

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
        "valor" : 2000,
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

@app.get('/productos/{codigo}')
def listadeproductos():
    return productos

@app.get('/productos/{codigo}')
def obtener_producto(codigo: int):
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto
    return {"mensaje": "Producto no encontrado"}

@app.get('/productos/{nombre}')
def obtener_producto_por_nombre(nombre: str):
    for producto in productos:
        if producto["nombre"] == nombre:
            return producto
    return {"mensaje": "Producto no encontrado"}

@app.post('/productos')
def crearProductos(
    codigo: int = Body(), 
    nombre: str = Body(), 
    valor: float = Body(), 
    existencia: int = Body()):
    productos.append({
        'codigo': codigo,
        'nombre': nombre,
        'valor': valor,
        'existencia': existencia
    })
    return productos

@app.post('/productos2')
def crearProductos2(
    codigo:int=Body(), 
    nombre:str=Body(), 
    valor:float=Body(), 
    existencia:int=Body()):
    productos.append({
        'codigo': codigo,
        'nombre': nombre,
        'valor': valor,
        'existencia': existencia
    }
    )
    return productos

@app.put('/productos/{codigo}')
def actualizar_producto(codigo: int, 
    nombre: str = Body(), 
    valor: float = Body(),
    existencia: int = Body()):
    for producto in productos:
        if producto['codigo'] == codigo:
            producto['nombre'] = nombre
            producto['valor'] = valor
            producto['existencia'] = existencia
            return producto
    return {"mensaje": "Producto no encontrado"}

@app.delete('/productos/{codigo}')
def eliminar_producto(codigo: int):
    for producto in productos:
        if producto['codigo'] == codigo:
            productos.remove(producto)
            return {"mensaje": "Producto eliminado"}
    return {"mensaje": "Producto no encontrado"}