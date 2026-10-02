from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["Cotización (HU 1)"])


@router.post("/cotizar", summary="Cotizar entradas de un evento y sector")
def cotizar():
    # TODO: implementar HU 1 (delegar en un servicio)
    raise HTTPException(status_code=501, detail="No implementado")