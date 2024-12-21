# -*- coding: utf-8 -*-
# Copyright 2024 Alejandro Olano <Github@alejo-code>


from fastapi import HTTPException


def calcular_factura(factura):
    # Calcular subtotal
    subtotal = sum(item.quantity * item.unit_price for item in factura.details)

    # Validación del subtotal
    if subtotal < 0:
        raise HTTPException(status_code=400, detail="El subtotal no puede ser negativo")

    iva = 0.0
    iva_porcentaje = 0

    if factura.type == "A":
        iva_porcentaje = 21
        iva = subtotal * 0.21
    elif factura.type == "B":
        iva_porcentaje = 10.5
        iva = subtotal * 0.105
    elif factura.type == "C":
        iva_porcentaje = 0
        # No se aplica IVA
    else:
        raise HTTPException(status_code=400, detail="Tipo de factura inválido")

    total = subtotal + iva
    return subtotal, iva_porcentaje, iva, total
