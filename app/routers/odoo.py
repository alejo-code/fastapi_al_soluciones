from fastapi import APIRouter
from app.odoo.services import get_partners

router = APIRouter()


@router.get("/partners", tags=["Odoo"])
def list_partners(limit: int = 10):
    """Obtener contactos de Odoo."""
    return {"partners": get_partners(limit=limit)}
