from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from enum import Enum

# Estados válidos para una reserva
class ReservationStatus(str, Enum):
    confirmed = "confirmed"
    cancelled = "cancelled"
    pending = "pending"

# Base de datos de reserva (entrada/salida común)
class ReservationBase(BaseModel):
    Hotel_Id: UUID
    Guest_Id: UUID
    Room_Id: UUID
    Check_In_Date: datetime
    Check_Out_Date: datetime
    Status: ReservationStatus

# Datos para crear una nueva reserva
class ReservationCreate(ReservationBase):
    pass

# Datos que se pueden actualizar en una reserva
class ReservationUpdate(BaseModel):
    Check_In_Date: datetime | None = None
    Check_Out_Date: datetime | None = None
    Status: ReservationStatus | None = None

# Respuesta completa con información adicional
class ReservationResponse(ReservationBase):
    Reservation_Id: UUID
    Create_at: datetime
    Update_at: datetime

    class Config:
        orm_mode = True
