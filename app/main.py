from fastapi import FastAPI
from app.routes import products, users, sales  # importamos nuestros módulos de rutas

# Inicializamos la aplicación FastAPI
app = FastAPI(
    title="ERP Básico con FastAPI",
    version="0.1",
    description="Esqueleto inicial de un ERP educativo"
)

# Conectamos las rutas de los diferentes módulos al app principal
app.include_router(products.router)
app.include_router(users.router)
app.include_router(sales.router)

# Endpoint raíz (solo para comprobar que funciona el servidor)
@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido al ERP Básico 🚀"}
