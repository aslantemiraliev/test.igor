from dotenv import load_dotenv
import os
from aiogram import Bot,Dispatcher
from database import Database
load_dotenv()

token = os.getenv('TOKEN')
bot = Bot(token=token)
dp = Dispatcher()
db = Database('db.sqlite3')