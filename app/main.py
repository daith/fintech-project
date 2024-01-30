# app/main.py

from fastapi import FastAPI
from .dependencies import calculate_square
from .stockItemList import stock_item_list

app = FastAPI()

@app.get("/square/{number}")
async def read_square(number: int):
    square_value = calculate_square(number)
    return {"number": number, "square": square_value}


@app.get("/stock/{action_type}")
async def read_square(action_type):
    job_date , stock_record_list = stock_item_list(action_type)
    return {"job_date": job_date, "stock_record_list": stock_record_list}