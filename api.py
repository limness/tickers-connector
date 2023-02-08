##################################################################################
# Copyright © 2022-2099 Andrew Tsyrkunov. All rights reserved
# Author: Andrew Tsyrkunov
# Contacts: <andrey.pwn@gmail.com>
##################################################################################
from datetime import datetime
from fastapi import FastAPI
from fastapi import status


app = FastAPI()


@app.get("/api/ping", status_code=status.HTTP_200_OK)
async def ping():
    return {"message": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
