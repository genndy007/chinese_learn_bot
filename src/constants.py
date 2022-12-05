import os
from dotenv import load_dotenv

load_dotenv('.env.prod')

BOT_TOKEN = os.getenv("BOT_TOKEN")
