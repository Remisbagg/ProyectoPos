import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Ruta absoluta al archivo de base de datos SQLite
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'database.sqlite')
DATABASE_URL = f"sqlite:///{os.path.abspath(DB_PATH)}"

# Motor de conexión con SQLite
engine = create_engine(DATABASE_URL, echo=True)

# Sesión para interactuar con la base de datos
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para los modelos ORM
Base = declarative_base()

# Dependencia para obtener sesión de base de datos en rutas
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
