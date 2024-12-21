# -*- coding: utf-8 -*-
# Copyright 2024 Alejandro Olano <Github@alejo-code>


from pydantic import BaseModel
from typing import List


class FacturaDetalle(BaseModel):
    product: str
    quantity: int
    unit_price: float


class FacturaRequest(BaseModel):
    type: str
    details: List[FacturaDetalle]
