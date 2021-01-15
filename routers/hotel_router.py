from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_connection import get_db

from db.hotel_db import HotelInDB

from models.hotel_models import HotelIn, HotelOut, HotelLog

router = APIRouter()

@router.get("/hotel/{hotelname}", response_model = HotelOut)
async def get_all_rooms(hotelname: str, db: Session = Depends(get_db)):
    hotel_in_db = db.query(HotelInDB).get(hotelname)

    if hotel_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El hotel no existe")

    return  hotel_in_db

'''
@router.post("/user/auth/")
async def auth_user(user_in: UserIn, db: Session = Depends(get_db)):

    user_in_db = db.query(UserInDB).get(user_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if user_in_db.password != user_in.password:
        raise HTTPException(status_code=403, detail="Error de autenticacion")

    return  {"Autenticado": True}

@router.get("/user/balance/{username}", response_model=UserOut)
async def get_balance(username: str, db: Session = Depends(get_db)):

    user_in_db = db.query(UserInDB).get(username)

    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")

    return  user_in_db
'''