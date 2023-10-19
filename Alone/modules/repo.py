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

**ᴏᴡɴᴇʀ  : [𝐀ʟᴏɴᴇ](https://t.me/ALONE_WAS_BOT)**
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
                        "Aʟᴏɴᴇ Mᴜsɪᴄ", url="https://github.com/TeamAloneOp/AloneXMusic/fork"
                    ),
                    InlineKeyboardButton(
                        "Aʟᴏɴᴇ Rᴏʙᴏᴛ", url="https://github.com/TeamAloneOp/AloneXRobot/fork"
                    ),
                ]
            ]
        ),
    )
