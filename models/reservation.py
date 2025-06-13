from sqlalchemy import Column, String, DateTime, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from datetime import datetime
from config.database import Base
import enum

# Estado posible de una reservación
class ReservationStatus(str, enum.Enum):
    confirmed = "confirmed"
    cancelled = "cancelled"
    pending = "pending"

# Modelo de base de datos para la entidad Reserva
class Reservation(Base):
    __tablename__ = "reservation"

    Reservation_Id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    Hotel_Id = Column(UUID(as_uuid=True), ForeignKey("hotel.Hotel_id"))
    Guest_Id = Column(UUID(as_uuid=True), ForeignKey("guest.Guest_id"))
    Room_Id = Column(UUID(as_uuid=True), ForeignKey("room.Room_id"))
    Check_In_Date = Column(DateTime)
    Check_Out_Date = Column(DateTime)
    Status = Column(Enum(ReservationStatus), default=ReservationStatus.pending)
    Create_at = Column(DateTime, default=datetime.utcnow)
    Update_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
