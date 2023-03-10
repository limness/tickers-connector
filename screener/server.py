##################################################################################
# Copyright © 2022-2099 Andrew Tsyrkunov. All rights reserved
# Author: Andrew Tsyrkunov
# Contacts: <andrey.pwn@gmail.com>
##################################################################################
import uvicorn
import sys
from loguru import logger
from app.api import app

logger.remove(0)
logger.add(sys.stderr, level="INFO", backtrace=True, diagnose=True)
logger.add("logs/outputs.log", level="DEBUG", backtrace=True, diagnose=True)


def start() -> None:
    uvicorn.run(
        app, host="0.0.0.0", port=8000,
        log_level="info"
    )


if __name__ == "__main__":
    start()

