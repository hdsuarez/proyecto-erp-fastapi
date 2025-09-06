from fastapi import APIRouter

router = APIRouter(
    prefix="/sales",
    tags=["Ventas"]
)

@router.get("/")
def get_sales():
    return {"mensaje": "Aquí listaríamos todas las ventas"}

@router.post("/")
def create_sale():
    return {"mensaje": "Aquí se registraría una nueva venta"}
