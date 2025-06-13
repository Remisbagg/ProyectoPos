from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from models.reservation import Reservation
from schemas.reservation import ReservationCreate, ReservationUpdate, ReservationResponse
from uuid import UUID

router = APIRouter(prefix="/reservations", tags=["Reservations"])

# Crear una nueva reserva
@router.post("/", response_model=ReservationResponse)
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    db_reservation = Reservation(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

# Obtener todas las reservas
@router.get("/", response_model=list[ReservationResponse])
def get_all_reservations(db: Session = Depends(get_db)):
    return db.query(Reservation).all()

# Obtener una reserva por ID
@router.get("/{reservation_id}", response_model=ReservationResponse)
def get_reservation(reservation_id: UUID, db: Session = Depends(get_db)):
    reservation = db.query(Reservation).filter(Reservation.Reservation_Id == reservation_id).first()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation

# Actualizar una reserva existente
@router.put("/{reservation_id}", response_model=ReservationResponse)
def update_reservation(reservation_id: UUID, updates: ReservationUpdate, db: Session = Depends(get_db)):
    reservation = db.query(Reservation).filter(Reservation.Reservation_Id == reservation_id).first()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(reservation, key, value)
    db.commit()
    db.refresh(reservation)
    return reservation

# Eliminar una reserva
@router.delete("/{reservation_id}")
def delete_reservation(reservation_id: UUID, db: Session = Depends(get_db)):
    reservation = db.query(Reservation).filter(Reservation.Reservation_Id == reservation_id).first()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    db.delete(reservation)
    db.commit()
    return {"detail": "Reservation deleted"}
