from app.odoo.connection import call_odoo


def get_partners(limit: int = 10):
    """Obtener una lista de contactos desde Odoo."""
    return call_odoo(
        "res.partner",
        "search_read",
        [],
        {"fields": ["id", "name", "email"], "limit": limit},
    )
