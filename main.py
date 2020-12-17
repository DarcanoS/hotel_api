from db.hotel_db import HotelInDB
from db.hotel_db import get_hotel,update_hotel, get_all_hotel
from models.hotel_models import HotelOut, HotelIn, HotelLog

import datetime
from fastapi import FastAPI
from fastapi import HTTPException


api = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080","https://hotel-app-s.herokuapp.com"
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@api.get("/hotel/rooms")
async def get_all_rooms():
    all_hotel = {}
    for key in get_all_hotel():
        hotel_out = HotelOut(**get_hotel(key).dict())
        all_hotel[hotel_out.hotelname] = hotel_out
    return all_hotel

@api.get("/hotel/description/{hotelname}")
async def get_room(hotelname: str):
    hotel_in_db = get_hotel(hotelname)
    if hotel_in_db == None:
        raise HTTPException(status_code=404, detail="El hotel no existe")
    hotel_out = HotelOut(**hotel_in_db.dict())
    return hotel_out

@api.post("/hotel/add")
async def add_hotel(hotel_in: HotelInDB):
    update_hotel(hotel_in)
    hotel_out = HotelOut(**hotel_in.dict())
    return hotel_out

@api.post("/hotel/login")
async def login_hotel(hotel_log: HotelLog):
    hotel_in_db = get_hotel(hotel_log.hotelname)
    hotel_log_password = hotel_log.password
    if hotel_in_db == None or hotel_log_password != hotel_in_db.password:
        raise HTTPException(status_code=404, detail="Usuario o contraseña incorrecta.")
    else:
        return  {"Autenticado": True}