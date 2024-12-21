import xmlrpc.client
from fastapi import HTTPException
from app.config import settings


def authenticate():
    """Autenticar el usuario en Odoo y obtener el UID."""
    try:
        common = xmlrpc.client.ServerProxy(f"{settings.ODOO_URL}/xmlrpc/2/common")
        uid = common.authenticate(
            settings.ODOO_DB, settings.ODOO_USER, settings.ODOO_PASSWORD, {}
        )
        if not uid:
            raise Exception("Credenciales inválidas")
        return uid
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error de autenticación: {e}")


def call_odoo(model: str, method: str, args: list, kwargs: dict = None):
    """Realizar llamadas al ORM de Odoo."""
    try:
        uid = authenticate()
        kwargs = kwargs or {}
        models = xmlrpc.client.ServerProxy(f"{settings.ODOO_URL}/xmlrpc/2/object")
        return models.execute_kw(
            settings.ODOO_DB, uid, settings.ODOO_PASSWORD, model, method, args, kwargs
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la llamada a Odoo: {e}")
