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