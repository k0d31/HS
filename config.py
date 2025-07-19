import os
from dotenv import load_dotenv

load_dotenv()

config = {
    "token": os.getenv("TOKEN")
}