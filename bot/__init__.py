#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int("12158462")

API_HASH = "0b962717d931f4480c46d56c85d409a5"

BOT_TOKEN = "5618135104:AAG0gwyVVffpXrYqEqRGBXAy6co5lglk0kA"

DB_URI = "mongodb+srv://thutafilter:thutafilter@thuta2023.znq8uex.mongodb.net/?retryWrites=true&w=majority"

USER_SESSION = "BQBkx2v2hjsupXAUHFzXjVq_oUNYLGmse8khbRuJz59pbeczR4z2N7KXEIytxJ8oR8BnzPseJ-J5QaHUVTwp2T7-SgqVIwqdMCyeycdSfVKzLQeSH1NvNJ_T-YUtDoT-CNOh91qlsxWsVw3IZgJTMX8usaPA0pKjdRn6BkcwmBwgTd_qPCfeWDfupreY2Ha_xCBft1pRews1_28ogcs9unU8dsfVLTg63d7y3OI1U7T3Wp825TcAtTNgO_xcn7q7Av09jJctPw0OOpMX6FDxgK4YKerpFmm7PkMDFm-aBsUrlgy2tbHFG6zlliZeNFpWq3Mo_4HZ_zlD0FCHZbNDrbS6UFsxVQA"

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
