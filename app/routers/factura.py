# -*- coding: utf-8 -*-
# Copyright 2024 Alejandro Olano <Github@alejo-code>

from fastapi import APIRouter
from app.models.factura import FacturaRequest
from app.services.factura_service import calcular_factura

router = APIRouter()


@router.post("/factura")
async def crear_factura(factura: FacturaRequest):
    # Calcular la factura
    subtotal, iva_porcentaje, iva, total = calcular_factura(factura)

    # Crear la respuesta con el resumen de la factura
    return {
        "type": factura.type,
        "subtotal": subtotal,
        "applied_tax": {"percentage": iva_porcentaje, "amount": iva},
        "total": total,
        "details": factura.details,
    }
