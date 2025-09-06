from fastapi import APIRouter

# Creamos un "router" (grupo de endpoints) para productos
router = APIRouter(
    prefix="/products",   # Todos los endpoints aquí empezarán con /products
    tags=["Productos"]    # Categoría que se mostrará en la documentación
)

# Endpoint GET básico
@router.get("/")
def get_products():
    return {"mensaje": "Aquí listaríamos todos los productos"}

# Endpoint POST básico
@router.post("/")
def create_product():
    return {"mensaje": "Aquí se crearía un nuevo producto"}
