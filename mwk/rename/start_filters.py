
import os
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from mwk.config import Config
from mwk.messages import Translation
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(filters.command("panduan"))
async def help_user(c,m):
    try:
       await m.reply_text(Translation.HELP_USER,quote=True)
    except Exception as e:
        log.info(str(e))
        
@Client.on_message(filters.command("start"))
async def start_msg(c,m):
    button = [
                [
                    InlineKeyboardButton(
                        "◈ADMIN◈", url=f"https://t.me/Zerozerozoro")
                ]
            ]
    markup = InlineKeyboardMarkup(button) 
    try:
       await m.reply_sticker(sticker="CAACAgUAAxkBAAED-FRiEQPzIKvlv10aV_McafmiKGeGggACVwQAAkqTyFcBGgj9cUrBOyME", quote=True)
       await m.reply_text(Translation.START_TEXT,quote=True,reply_markup=markup,disable_web_page_preview=True) 
    except Exception as e:
        log.info(str(e))
        
@Client.on_message(filters.command("catatan") & filters.private & filters.user(Config.OWNER_ID))
async def log_msg(c,m):
  z =await m.reply_text("Processing..", True)
  if os.path.exists("Log.txt"):
     await m.reply_document("Catatan.txt", True)
     await z.delete()
  else:
    await z.edit_text("Log file not found")
