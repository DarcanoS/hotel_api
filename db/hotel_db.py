from sqlalchemy import Column, Integer, String
from db.db_connection import Base, engine

class HotelInDB(Base):
    __tablename__ = "hotel"

    hotelname = Column(String, primary_key = True, unique = True)
    password = Column(String)
    location = Column(String)
    price_general = Column(Integer)
    quantity_room = Column(Integer)
    
Base.metadata.create_all(bind=engine)


'''
from typing import Dict
from pydantic import BaseModel

class HotelInDB(BaseModel):
    hotelname: str
    password: str
    location: str
    price_general: int
    quantity_room: int

database_hotel = Dict[str, HotelInDB]

database_hotel = {
    "Caminos": HotelInDB(**{"hotelname":"Caminos",
                        "password":"root",
                        "location":"Bogota",
                        "price_general":65000,
                        "quantity_room":18}),
    "El lago": HotelInDB(**{"hotelname":"El lago",
                        "password":"1234",
                        "location":"Medellin",
                        "price_general":70000,
                        "quantity_room":12})
}

def get_hotel(name: str):
    if name in database_hotel.keys():
        return database_hotel[name]
    else:
        return None

def update_hotel(hotel: HotelInDB):
    database_hotel[hotel.hotelname] = hotel
    return hotel

def get_all_hotel():
    return database_hotel

def delete_hotel(name: str):
    if name in database_hotel.keys():
        del database_hotel[name]
        return "Eliminado"
    else:
        return "Usuario no existente"
'''