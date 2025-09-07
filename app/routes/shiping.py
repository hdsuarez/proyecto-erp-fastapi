# app/routes/shipping.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/shipping", tags=["Shipping"])

# Modelo de request - qué datos esperamos cuando creamos un envío
class ShippingRequest(BaseModel):
    order_id: int           # id del pedido en nuestro ERP
    courier: str            # 'dhl', 'servientrega', 'interrapidisimo', 'envia'
    weight_kg: float        # peso del paquete (ej: 1.5)
    address: str            # dirección de entrega (simplificado)

# Modelo de response - lo que devolvemos al crear una guía
class ShippingResponse(BaseModel):
    status: str             # 'created' | 'error'
    tracking_number: str | None = None
    message: str

@router.post("/create", response_model=ShippingResponse)
def create_shipment(req: ShippingRequest):
    """
    Endpoint simulado para crear una guía de envío.
    - No llama a APIs externas reales.
    - Genera un 'tracking_number' ficticio según courier y order_id.
    """
    courier = req.courier.lower()
    # Lógica de simulación sencilla por courier
    if courier == "dhl":
        tracking = f"DHL-{req.order_id:06d}"
    elif courier == "servientrega":
        tracking = f"SV-{req.order_id:06d}"
    elif courier == "interrapidisimo":
        tracking = f"IR-{req.order_id:06d}"
    elif courier == "envia":
        tracking = f"EN-{req.order_id:06d}"
    else:
        # Courier no soportado por la simulación
        raise HTTPException(status_code=400, detail="Courier no soportado en el entorno simulado")

    # En un sistema real aquí llamaríamos a la API del courier y guardaríamos la guía en BD
    return ShippingResponse(
        status="created",
        tracking_number=tracking,
        message=f"Guía simulada creada para {req.courier}"
    )

@router.get("/status/{tracking}", response_model=ShippingResponse)
def get_status(tracking: str):
    """
    Consulta de estado simulada.
    - Devuelve estados fijos según patrón de tracking.
    """
    # Ejemplo simple: estado 'in_transit' si contiene 'DHL', 'delivered' si termina en '0'
    if tracking.upper().startswith("DHL"):
        state = "in_transit"
    elif tracking.upper().startswith("SV"):
        state = "in_transit"
    elif tracking.upper().startswith("IR"):
        state = "in_transit"
    elif tracking.upper().startswith("EN"):
        state = "in_transit"
    else:
        raise HTTPException(status_code=404, detail="Tracking no encontrado (simulado)")

    return ShippingResponse(status=state, tracking_number=tracking, message="Estado simulado")
