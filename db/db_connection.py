from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Crear motor y la conexion con la DB
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:7997@localhost:5432/MISION_TIC"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#Crear la sesion
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Creando Base para la creacion de los modelos
Base= declarative_base()
Base.metadata.schema = "Ciclo_III"