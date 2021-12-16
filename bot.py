import json
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv
from os.path import join, dirname
from config import BaseConfig

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
# Get ENV
get_config = BaseConfig()

# Initialize bot
bot = Bot(token=get_config.TELEGRAM_API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


# Helpers

# Get args from telegram command
def extract_arg(arg):
    return arg.split()[1:]


# Commands
@dp.message_handler()
async def handle_commands(message: types.Message):
    print(message["chat"]["id"])
# Start command
# @dp.message_handler(commands=['start'])
# async def process_start_command(message: types.Message):
#     # Get chat id
#     chat_id = message['chat']['id']
#     json_db = None
#     with open('db/db.json', 'r') as db:
#         json_db = json.load(db)
#     if json_db['chats']:
#         # Get chat list
#         chats_list = json_db['chats']
#         # Find chat
#         find_chat = [item for item in chats_list if item["chat_id"] == chat_id]
#         if not find_chat:
#             # Update chats list
#             chats_list.append({
#                 "chat_id": chat_id
#             })
#             # Update file
#             with open('db/db.json', 'w') as db:
#                 json.dump({
#                     "chats": chats_list
#                 }, db)
#     else:
#         with open('db/db.json', 'w') as db:
#             json.dump({
#                 "chats": [
#                     {
#                         "chat_id": chat_id
#                     }
#                 ]
#             }, db)


# Start bot
if __name__ == '__main__':
    executor.start_polling(dp)
