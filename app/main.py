from fastapi import FastAPI
from app.routers import odoo

app = FastAPI(title="FastAPI + Odoo App")

# Registrar los routers
app.include_router(odoo.router, prefix="/odoo", tags=["Odoo"])


@app.get("/")
def root():
    return {"message": "Bienvenido a la integración FastAPI + Odoo"}
