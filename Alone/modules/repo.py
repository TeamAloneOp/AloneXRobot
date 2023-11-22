# ""DEAR PRO PEOPLE,  DON'T REMOVE & CHANGE THIS LINE
# TG :- @ALONE_WAS_BOT
#     MY ALL BOTS :- AloneXBots
#     GITHUB :- TEAMALONEOP ""

from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from Alone import AloneX as pbot

AloneXX = "https://telegra.ph//file/9e8ce3092848a1bc5d9d6.jpg"


@pbot.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_photo(
        photo=AloneXX,
        caption=f"""✨ **ʜᴇʏ {message.from_user.mention},**

**ᴏᴡɴᴇʀ  : [𝐀ʟᴏɴᴇ](\x68\x74\x74\x70\x73\x3A\x2F\x2F\x74\x2E\x6D\x65\x2F\x41\x4C\x4F\x4E\x45\x5F\x57\x41\x53\x5F\x42\x4F\x54)**
**ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :** `{y()}`
**ʟɪʙʀᴀʀʏ ᴠᴇʀꜱɪᴏɴ :** `{o}`
**ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :** `{s}`
**ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪᴏɴ :** `{z}`
** ᴇɴᴊᴏʏ**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aʟᴏɴᴇ Mᴜsɪᴄ", url="\x68\x74\x74\x70\x73\x3A\x2F\x2F\x67\x69\x74\x68\x75\x62\x2E\x63\x6F\x6D\x2F\x54\x65\x61\x6D\x41\x6C\x6F\x6E\x65\x4F\x70\x2F\x41\x6C\x6F\x6E\x65\x58\x4D\x75\x73\x69\x63"
                    ),
                    InlineKeyboardButton(
                        "Aʟᴏɴᴇ Rᴏʙᴏᴛ", url="\x68\x74\x74\x70\x73\x3A\x2F\x2F\x67\x69\x74\x68\x75\x62\x2E\x63\x6F\x6D\x2F\x54\x65\x61\x6D\x41\x6C\x6F\x6E\x65\x4F\x70\x2F\x41\x6C\x6F\x6E\x65\x52\x6F\x62\x6F\x74"
                    ),
                ]
            ]
        ),
    )
