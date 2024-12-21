# Factura API

Factura API es un proyecto desarrollado con FastAPI para gestionar la generación de facturas. La API permite calcular el subtotal, el IVA y el total de las facturas, según el tipo especificado (A, B o C). Este proyecto está diseñado para ser modular, organizado y escalable.

---

## Características

- **Cálculo automático de IVA según el tipo de factura:**
  - Factura A: 21% de IVA.
  - Factura B: 10.5% de IVA.
  - Factura C: No aplica IVA.
- **Validaciones** para garantizar que los datos de entrada sean correctos.
- **Respuesta detallada** con un resumen de la factura.

---

## Requisitos

- Python 3.8 o superior.
- Dependencias especificadas en `requirements.txt`.

---

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/factura_api.git
   cd factura_api
   ```

2. Crea un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta la aplicación:

   ```bash
   uvicorn app.main:app --reload
   ```

---

## Uso

### Endpoint disponible

**POST /factura**

#### Solicitud:

```json
{
  "type": "A",
  "details": [
    { "product": "Producto X", "quantity": 2, "unit_price": 250.0 },
    { "product": "Servicio Y", "quantity": 1, "unit_price": 500.0 }
  ]
}
```

#### Respuesta:

```json
{
  "type": "A",
  "subtotal": 1000,
  "applied_tax": {
    "percentage": 21,
    "amount": 210
  },
  "total": 1210,
  "details": [
    { "product": "Producto X", "quantity": 2, "unit_price": 250.0 },
    { "product": "Servicio Y", "quantity": 1, "unit_price": 500.0 }
  ]
}
```

### Documentación interactiva

Una vez que la aplicación esté en ejecución, puedes acceder a la documentación interactiva en:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Estructura del proyecto

```plaintext
factura_api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── factura.py
│   │   └── producto.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── factura_service.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── factura.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
├── requirements.txt
└── README.md
```

---

## Pruebas

Para probar la API, puedes usar herramientas como [Postman](https://www.postman.com/) o `curl`.

Ejemplo con `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/factura" \
-H "Content-Type: application/json" \
-d '{
  "type": "A",
  "details": [
    {"product": "Producto X", "quantity": 2, "unit_price": 250.0},
    {"product": "Servicio Y", "quantity": 1, "unit_price": 500.0}
  ]
}'
```

---
