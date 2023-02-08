##################################################################################
# Copyright © 2022-2099 Andrew Tsyrkunov. All rights reserved
# Author: Andrew Tsyrkunov
# Contacts: <andrey.pwn@gmail.com>
##################################################################################
import global_vars
from datetime import datetime
from fastapi import FastAPI
from fastapi import Response
from fastapi import status
from utils import init_tickers


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    # Initialize allowed tickers before opening connections
    init_tickers()

    # Initialize all sockets
    # asyncio.create_task(socket())


@app.get("/api/ping", status_code=status.HTTP_200_OK)
async def ping():
    return {"message": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}


@app.get("/api/courses", status_code=status.HTTP_200_OK)
async def get_courses():
    return global_vars.tickers


@app.get("/api/courses/{ticker}", status_code=status.HTTP_200_OK)
async def get_course(ticker: str, response: Response):
    if ticker not in global_vars.tickers:
        response.status_code = 404
        return {"message": f"Ticker with name `{ticker}` not exists!"}
    return global_vars.tickers[ticker]
