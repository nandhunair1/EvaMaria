import os
import logging
from bs4 import BeautifulSoup
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.command("cs"))
async def score(_, message):
    m = await message.reply_text("`Gathering ongoing match scorecard...`")
    try:       
        url = "https://www.espncricinfo.com/live-cricket-score"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        
        match_descrition = soup.select(".description")
        obj1 = soup.select(".teams")
        status = soup.select(".status-text")
        text = ""
        text = text + "**🔴 𝐋𝐈𝐕𝐄 𝐒𝐂𝐎𝐑𝐄 🏏**\n\n" + f"**{match_descrition[0].text}**" + "\n\n" + f"**⦿ {status[0].text}**" + "\n\n" + f"**® {obj1[0].text}**" + "\n\n" + "©️ MᴀɪɴᴛᴀɪɴᴇD Bʏ : <a href='https://t.me/tvseriezzz'>♠️ 𝑨𝒍𝒍 𝑰𝒏 𝑶𝒏𝒆 𝑮𝒓𝒐𝒖𝒑 🎬</a>"
        text = text.replace("Check ", "")
        text = text.replace("(", " (")
        text = text.replace(")", ") ")
        await m.edit(text, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(
                                [[InlineKeyboardButton(
                                     "♻️ ⒼⓇⓄⓊⓅ ♻️", url="https://t.me/tvseriezzz")]]))
        return
    except Exception as e:
        print(str(e))
        return await m.edit("`No any ongoing matches at this time.`")

