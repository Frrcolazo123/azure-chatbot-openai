from sqlalchemy import Column, Integer, String
from config.database import Base

class Usuarios(Base):
    __tablename__ = "Usuarios"

    id = Column(Integer, primary_key = True)
    apellido = Column(String(20))
    nombre= Column(String(20))
    correo= Column(String(100))
    password=Column(String(1000))
