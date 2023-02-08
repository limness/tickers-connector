##################################################################################
# Copyright © 2022-2099 Andrew Tsyrkunov. All rights reserved
# Author: Andrew Tsyrkunov
# Contacts: <andrey.pwn@gmail.com>
##################################################################################
import uvicorn
from app.api import app


def start() -> None:
    uvicorn.run(
        app, host="0.0.0.0", port=8000,
        log_level="info"
    )


if __name__ == "__main__":
    start()

