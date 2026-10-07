from pydantic import BaseModel, ConfigDict
from datetime import datetime

# --- LUGAR ---
class LugarBase(BaseModel):
    nombre: str
    direccion: str

class LugarCreate(LugarBase):
    pass

class LugarResponse(LugarBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# --- CLIENTE ---
class ClienteBase(BaseModel):
    nombre: str
    email: str

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# --- EVENTO ---
class EventoBase(BaseModel):
    nombre: str
    fecha: datetime
    lugar_id: int

class EventoCreate(EventoBase):
    pass

class EventoResponse(EventoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)