import enum
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class EstadoEntrada(str, enum.Enum):
    DISPONIBLE = "Disponible"
    RESERVADA = "Reservada"
    EMITIDA = "Emitida"
    UTILIZADA = "Utilizada"


class EstadoVenta(str, enum.Enum):
    PENDIENTE = "Pendiente"
    PAGADA = "Pagada"
    CANCELADA = "Cancelada"


class Lugar(Base):
    __tablename__ = "lugares"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    direccion: Mapped[str] = mapped_column(String(200))

    sectores: Mapped[list["Sector"]] = relationship(back_populates="lugar")
    eventos: Mapped[list["Evento"]] = relationship(back_populates="lugar")


class Sector(Base):
    __tablename__ = "sectores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    capacidad_maxima: Mapped[int] = mapped_column(Integer)
    lugar_id: Mapped[int] = mapped_column(ForeignKey("lugares.id"))

    lugar: Mapped["Lugar"] = relationship(back_populates="sectores")


class Evento(Base):
    __tablename__ = "eventos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    fecha: Mapped[datetime] = mapped_column(DateTime)
    lugar_id: Mapped[int] = mapped_column(ForeignKey("lugares.id"))

    lugar: Mapped["Lugar"] = relationship(back_populates="eventos")
    precios: Mapped[list["PrecioSector"]] = relationship(back_populates="evento")
    entradas: Mapped[list["Entrada"]] = relationship(back_populates="evento")


class PrecioSector(Base):
    """Precio de un sector para un evento en particular."""
    __tablename__ = "precios_sector"

    id: Mapped[int] = mapped_column(primary_key=True)
    precio: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    evento_id: Mapped[int] = mapped_column(ForeignKey("eventos.id"))
    sector_id: Mapped[int] = mapped_column(ForeignKey("sectores.id"))

    evento: Mapped["Evento"] = relationship(back_populates="precios")
    sector: Mapped["Sector"] = relationship()


class Cliente(Base):
    __tablename__ = "clientes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(120), unique=True)

    ventas: Mapped[list["Venta"]] = relationship(back_populates="cliente")


class Venta(Base):
    __tablename__ = "ventas"

    id: Mapped[int] = mapped_column(primary_key=True)
    estado: Mapped[EstadoVenta] = mapped_column(
        Enum(EstadoVenta), default=EstadoVenta.PENDIENTE
    )
    fecha: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    total: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=0)
    cliente_id: Mapped[int] = mapped_column(ForeignKey("clientes.id"))

    cliente: Mapped["Cliente"] = relationship(back_populates="ventas")
    entradas: Mapped[list["Entrada"]] = relationship(back_populates="venta")


class Entrada(Base):
    __tablename__ = "entradas"

    id: Mapped[int] = mapped_column(primary_key=True)
    codigo_qr: Mapped[str] = mapped_column(String(64), unique=True)
    estado: Mapped[EstadoEntrada] = mapped_column(
        Enum(EstadoEntrada), default=EstadoEntrada.DISPONIBLE
    )
    hora_ingreso: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    evento_id: Mapped[int] = mapped_column(ForeignKey("eventos.id"))
    sector_id: Mapped[int] = mapped_column(ForeignKey("sectores.id"))
    venta_id: Mapped[int | None] = mapped_column(ForeignKey("ventas.id"), nullable=True)

    evento: Mapped["Evento"] = relationship(back_populates="entradas")
    sector: Mapped["Sector"] = relationship()
    venta: Mapped["Venta | None"] = relationship(back_populates="entradas")