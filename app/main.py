from fastapi import FastAPI

from app import models  # noqa: F401  (registra las tablas)
from app.database import Base, engine
from app.routers import acceso, cotizacion, pagos

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SmartTicket API",
    description="Gestión de eventos y control de acceso",
    version="0.1.0",
)

app.include_router(cotizacion.router)
app.include_router(pagos.router)
app.include_router(acceso.router)