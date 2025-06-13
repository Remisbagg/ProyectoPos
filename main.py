from fastapi import FastAPI
from routes import reservation
from models.reservation import Base as ReservationBase
from config.database import engine

app = FastAPI()

# Crear las tablas si no existen
ReservationBase.metadata.create_all(bind=engine)

# Incluir routers de endpoints
app.include_router(reservation.router)
