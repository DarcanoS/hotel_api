from pydantic import BaseModel

class HotelIn(BaseModel):
    hotelname: str
    password: str
    location: str
    price_general: int
    quantity_room: int

class HotelOut(BaseModel):
    hotelname: str
    price_general: int
    quantity_room: int

class HotelLog(BaseModel):
    hotelname: str
    password: str
