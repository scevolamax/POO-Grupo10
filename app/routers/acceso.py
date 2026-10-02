from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["Acceso (HU 3)"])


@router.post("/escanear-acceso", summary="Escanear el QR de una entrada en puerta")
def escanear_acceso():
    # TODO: implementar HU 3 (delegar en un servicio)
    raise HTTPException(status_code=501, detail="No implementado")