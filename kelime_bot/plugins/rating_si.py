from kelime_bot import rating
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message


@Client.on_message(filters.command("skor"))
async def ratingsa(c:Client, m:Message):
    global rating
    metin = """\n📝 **Küresel Oyuncu Sıralaması ** \n🏆 :

"""
    list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    eklenen = 0
    puanlar = []
    for kisi in rating:
        puanlar.append(rating[kisi])
    puanlar.sort(reverse = True)
    for puan in puanlar:
        for kisi in rating:
            if puan == rating[kisi]:
                metin += f"**{kisi}** : {puan}  Puan\n"
                eklenen += 1
                if eklenen == 20:
                    for i in range (1, 20):
                         if puan == rating[kisi]:
                            metin += f"**{i}** : 
                            if eklenen == 20:
                                       break
                
    await c.send_message(m.chat.id, metin)
