#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 21970953
API_HASH = "914f964d0e1e15b1627b33e1d2ea35bd"
BOT_TOKEN = "6117381690:AAEpf113HHPlyYqDHWiS97lrQ4GRTPf99-0"
SESSION = "BQFPQAkAb8opqzXFA7qtqXfvSAc8XCHG369xunogKtMNMiOVWvzDSaQMkr3mIScjGl7Bm8NlbXAb14ydXM_HA-RtLM3EdZLrQW0AUlgJgD7-pPyNq2sbvQPntTLv88zQj03cgvELsEptiFRVwqZZrYC-tuS20z4QpF3DD15tOHJowoeXxibzKAQ-VrCGlVfNV2CDU8Abruhh263HW8AQRJ_qEG-vd_OOwJEJXjFn9xkwDBtmN9vFwBLlH9A-VKJu9n2jFVXMrj_wPYIAaYam0QvavvGBjqFzrsdt3ypZ1efXjnn_8LZ_sXZvnIvsbuDV2mVvcMJFpEYrT7Xono5-LQdUnWfvRwAAAAF-AMX3AA"
FORCESUB = "wickjohn000777"
AUTH = 6408947191

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
