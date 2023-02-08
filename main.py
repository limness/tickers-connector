##################################################################################
# Copyright © 2022-2099 Andrew Tsyrkunov. All rights reserved
# Author: Andrew Tsyrkunov
# Contacts: <andrey.pwn@gmail.com>
##################################################################################
import uvicorn
from app.api import app


def start() -> None:
    uvicorn.run(
        app, host="localhost", port=8000,
        log_level="info"#, log_config=f"log.ini"
    )


if __name__ == "__main__":
    start()

