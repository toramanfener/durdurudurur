from pyrogram import Client
from pyrogram import filters
from random import shuffle
from kelime_bot import USERNAME
from pyrogram.types import Message
from kelime_bot.helpers.keyboards import *
from kelime_bot.helpers.kelimeler import kelime_sec
from kelime_bot import *



@Client.on_message(filters.command("cancel") & ~filters.private & ~filters.channel)
async def stop(c:Client, m:Message):
    global oyun
    
    siralama = []
    for i in oyun[m.chat.id]["oyuncular"]:
        siralama.append(f'{i}   :   {oyun[m.chat.id]["oyuncular"][i]} ๐ฏ๐๐บ๐')
    siralama.sort(reverse=True)
    siralama_text = ""
    for i in siralama:
        siralama_text += i + "\n"     
    
    await c.send_message(m.chat.id, f"**{m.from_user.mention}** ๐ณ๐บ๐๐บ๐ฟ๐๐๐ฝ๐บ๐ ! \n ๐ฎ๐๐๐ Sonlandฤฑrฤฑldฤฑ! \n ๐ธ๐พ๐๐ ๐ฎ๐๐๐ ๐ก๐บ๐๐๐บ๐๐๐บ๐ ๐๐ผ๐๐ \n /game ๐ธ๐บ๐๐บ๐ป๐๐๐๐๐๐๐๐๐ . . .\n\n ๐ ๐ฏ๐๐บ๐ ๐ณ๐บ๐ป๐๐๐๐  :\n\n{siralama_text}")
    oyun[m.chat.id] = {}
    
