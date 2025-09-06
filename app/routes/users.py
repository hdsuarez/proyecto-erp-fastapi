from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Usuarios"]
)

@router.get("/")
def get_users():
    return {"mensaje": "Aquí listaríamos todos los usuarios"}

@router.post("/")
def create_user():
    return {"mensaje": "Aquí se registraría un nuevo usuario"}
