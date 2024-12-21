# -*- coding: utf-8 -*-
# Copyright 2024 Alejandro Olano <Github@alejo-code>

from fastapi import FastAPI
from app.routers.factura import router as factura_router

app = FastAPI()

# Incluir las rutas
app.include_router(factura_router)
