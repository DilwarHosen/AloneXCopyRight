from pyrogram import Client, filters
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters
from pyrogram.types import Message
import time
import psutil
import platform
import logging
from config import OWNER_ID, BOT_USERNAME
from config import *
from COPYRIGHT2 import COPYRIGHT2 as app

import pyrogram
from pyrogram.errors import FloodWait


# ----------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------


start_txt = """<b> 🤖 𝖠𝗅𝗈𝗇𝖾 𝖢𝗈𝗉𝗒𝖱𝗂𝗀𝗁𝗍 𝖱𝗈𝖻𝗈𝗍 🛡️ </b>

𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 𝖠𝗅𝗈𝗇𝖾 𝖢𝗈𝗉𝗒𝖱𝗂𝗀𝗁𝗍 𝖡𝗈𝗍, 𝗒𝗈𝗎𝗋 𝗏𝗂𝗀𝗂𝗅𝖺𝗇𝗍 𝗀𝗎𝖺𝗋𝖾𝗂𝗇 𝗂𝗇 𝗍𝗁𝗂𝗌 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝗌𝗉𝖺𝖼𝖾! 𝖮𝗎𝗋 𝗆𝗂𝗌𝗌𝗂𝗈𝗇 𝗂𝗌 𝗍𝗈 𝖾𝗇𝗌𝗎𝗋𝖾 𝖺 𝗌𝖾𝖼𝗎𝗋𝖾 𝖺𝗇𝖽 𝗉𝗅𝖾𝖺𝗌𝖺𝗇𝗍 𝖾𝗇𝗏𝗂𝗋𝗈𝗇𝗆𝖾𝗇𝗍 𝖿𝗈𝗋 𝖾𝗏𝖾𝗋𝗒𝗈𝗇𝖾. 𝖥𝗋𝗈𝗆 𝖼𝗈𝗉𝗒𝗋𝗂𝗀𝗁𝗍 𝗉𝗋𝗈𝗍𝖾𝖼𝗍𝂢𝗂𝗈𝗇 𝗍𝗈 𝗆𝖺𝗂𝗇𝗍𝖺𝗂𝗇𝗂𝗇𝗀 𝖽𝖾𝖼𝗈𝗋𝗎𝗆, 𝗐𝖾'𝗏𝖾 𝗀𝗈𝗍 𝗂𝗍 𝖼𝗈𝗏𝖾𝗋𝖾𝖽.

𝖥𝖾𝖾𝗅 𝖿𝗋𝖾𝖾 𝗍𝗈 𝗋𝖾𝗉𝗈𝗿𝗍 𝖺𝗇𝗒 𝖼𝗈𝗇𝖼𝖾𝗋𝗇𝗌, 𝖺𝗇𝖽 𝗅𝖾𝗍'𝗌 𝗐𝗈𝗋𝗄 𝗍𝗈𝗀𝖾𝗍𝗁𝖾𝗋 𝗍𝗈 𝗆𝖺𝗄𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝗎𝗇𝗂𝗍𝗒 𝗍𝗁𝗋𝗂𝗏𝖾! 🤝🔐 """

@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("❍ 𝐀ᴅᴅ 𝐌ᴇ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ ❍", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("❍ 𝐎ᴡɴᴇʀ ❍", user_id=OWNER_ID),
          InlineKeyboardButton("❍ 𝐔ᴘᴅᴀᴛᴇ ❍", url="https://t.me/AloneXBots"),    
        ]
        ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/msi8bw.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )


gd_buttons = [              
        [
            InlineKeyboardButton("❍ 𝐎ᴡɴᴇʀ ❍", user_id=OWNER_ID),
            InlineKeyboardButton("❍ 𝐔ᴘᴅᴀᴛᴇ ❍", url="https://t.me/AloneXBots"),    
        ]
        ]


# ------------------------------------------------------------------------------- #


@app.on_callback_query(filters.regex("dil_back"))
async def dil_back(_, query: CallbackQuery):
    await query.message.edit_caption(start_txt,
                                    reply_markup=InlineKeyboardMarkup(gd_buttons),)
        

# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------


start_time = time.time()

def time_formatter(milliseconds: float) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

def size_formatter(bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            break
        bytes /= 1024.0
    return f"{bytes:.2f} {unit}"



@app.on_message(filters.command("ping"))
async def activevc(_, message: Message):
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    storage = psutil.disk_usage('/')

    python_version = platform.python_version()

    reply_text = (
        f"➪ᴜᴘᴛɪᴍᴇ: {uptime}\n"
        f"➪ᴄᴘᴜ: {cpu}%\n"
        f"➪ꜱᴛᴏʀᴀɢᴇ: {size_formatter(storage.total)} [ᴛᴏᴛᴀʟ]\n"
        f"➪{size_formatter(storage.used)} [ᴜsᴇᴅ]\n"
        f"➪{size_formatter(storage.free)} [ғʀᴇᴇ]\n"
        f"➪ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ: {python_version},"
    )

    await message.reply(reply_text, quote=True)


    
# -------------------------------------------------------------------------------------



FORBIDDEN_KEYWORDS = ["porn", "xxx", "sex", "NCERT", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "chutmaarfucker", "maadharpille", "maadharchod", "investment", "maderchodo", ".replyraid", "fingering", "maderchod", "betichod", "bhenchod", "bhsdwale", "!bigspam", ".bigspam", "earnings", "fingring", "gandmara", "https://", "invested", "maachuda", "religion", "asshole", "bechara", "bhnchod", "earning", "/kickme", "@nnbbot", "savings", "selling", "service", "sexchat", "trading", "bhosda", "chuchi", ".clone", "comics", ".gcast", "inches", "invest", "offers", "prices", "randii", "randwa", "saving", "vagina", "vagins", "vegina", "bsdkk", "chodu", "chudd", "chumt", "comic", "d'esi", "doodh", "gaand", "gandu", "horny", "jhant", "jhatu", "laude", "money", "mulla", "mulle", "nudes", "penis", ".ping", ".pong", "price", "pussy", ".raid", "randi", ".spam", "totla", "trade", "video", "vosra", "alle", "boob", "bsdk", "chod", "chut", "desi", "dick", "earn", "fuck", "gali", "gand", "link", "lode", "lumd", "lund", "mode", "nude", "paid", "por*", "porn", "semx", "slut", "suck", "tmck", "tmkc", "bio", "btc", "d.m", "fed", "gay", "maa", "por", "sex", "ssn", "s*x", "bc", "ct", "dm", "mc", "$"]

@app.on_message()
async def handle_message(client, message):
    if any(keyword in message.text for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
      #  user_mention = from_user.mention
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")
    elif any(keyword in message.caption for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
       # user_mention = from_user.mention
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")
        
        
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    if any(keyword in message.text for keyword in FORBIDDEN_KEYWORDS):
        await edited_message.delete()
#  user_mention = from_user.mention
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝖤𝖽𝗂𝗍𝗂𝗇𝗀 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")
    elif any(keyword in message.caption for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
       # user_mention = from_user.mention
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝖤𝖽𝗂𝗍𝗂𝗇𝗀 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")


# ----------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
def delete_long_messages(_, m):
    return len(m.text.split()) > 10

@app.on_message(filters.group & filters.private & delete_long_messages)
async def delete_and_reply(_, msg):
    await msg.delete()
    user_mention = msg.from_user.mention
    await app.send_message(msg.chat.id, f"Hey {user_mention}, please keep your messages short!")
    

# -----------------------------------------------------------------------------------


    
@app.on_message(filters.animation | filters.audio | filters.document | filters.photo | filters.sticker | filters.video)
async def keep_reaction_message(client, message: Message):
    pass 
# -------------------------------

async def delete_pdf_files(client, message):
    if message.document and message.document.mime_type == "application/pdf":
        warning_message = f"@{message.from_user.username} ᴍᴀᴀ ᴍᴀᴛ ᴄʜᴜᴅᴀ ᴘᴅғ ʙʜᴇᴊ ᴋᴇ,\n ʙʜᴏsᴀᴅɪᴋᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀɢʏᴇɢᴀ \n\n ᴅᴇʟᴇᴛᴇ ᴋᴀʀ ᴅɪʏᴀ ᴍᴀᴅᴀʀᴄʜᴏᴅ.\n\n ᴀʙ @iam_daxx ʙʜᴀɪ ᴋᴇ ᴅᴍ ᴍᴇ ᴀᴘɴɪ ᴍᴜᴍᴍʏ ᴋᴏ ʙʜᴇᴊ ᴅᴇ 🍌🍌🍌."
        await message.reply_text(warning_message)
        await message.delete()
    else:  
        pass

@app.on_message(filters.group & filters.document)
async def message_handler(client, message):
    await delete_pdf_files(client, message)

# ----------------------------------------
