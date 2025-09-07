from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, database

app = FastAPI(title="ERP Básico con BD", version="0.2")

# Crear tablas en la BD automáticamente
models.Base.metadata.create_all(bind=database.engine)

# Dependencia para obtener sesión de BD
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido al ERP con Base de Datos 🚀"}

# --- Usuarios ---
@app.post("/usuarios/")
def crear_usuario(nombre: str, db: Session = Depends(get_db)):
    nuevo_usuario = models.Usuario(nombre=nombre)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@app.get("/usuarios/")
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(models.Usuario).all()
