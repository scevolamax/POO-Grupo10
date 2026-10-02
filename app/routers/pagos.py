from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["Pagos (HU 2)"])


@router.post("/iniciar-pago", summary="Iniciar el pago de una cotización")
def iniciar_pago():
    # TODO: implementar HU 2 (delegar en un servicio)
    raise HTTPException(status_code=501, detail="No implementado")


@router.post("/webhook-pagos", summary="Webhook de la pasarela de pagos")
def webhook_pagos():
    # TODO: implementar HU 2
    raise HTTPException(status_code=501, detail="No implementado")
