from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot.helpers.keyboards import *
from kelime_bot.helpers.kelimeler import kelime_sec
from kelime_bot import *



@Client.on_message(filters.command("pass") & ~filters.private & ~filters.channel)
async def passs(c:Client, m:Message):
    global oyun
    
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        if oyun[m.chat.id]["pass"] < 3:
            oyun[m.chat.id]["pass"] += 1 
            await c.send_message(m.chat.id,f"š š³ššššŗš 3 ššŗšš ššŗšššššš ššŗšš½šš !\nš„³ šŖš¾šššš¾ šÆšŗš š¦š¾š¼ššš½š !\nāļø š£šššš šŖš¾šššš¾ : **<code>{oyun[m.chat.id]['kelime']}</code>**")
            
            oyun[m.chat.id]["kelime"] = kelime_sec()
            oyun[m.chat.id]["aktif"] = True
            
            kelime_list = ""
            kelime = list(oyun[m.chat.id]['kelime'])
            shuffle(kelime)
            
            for harf in kelime:
                kelime_list+= harf + " "
            
            text = f"""
šÆ š±šŗššš½ : {oyun[m.chat.id]['round']}/60 
š šŖš¾šššš¾ :   <code>{kelime_list}</code>
š° šŖšŗššŗšš½šššŗš¼šŗš šÆššŗš : 1
š Ä°ššš¼š : 1. {oyun[m.chat.id]["kelime"][0]}
āš» š“šššššš : {int(len(kelime_list)/2)} 

āļø šŖšŗššššš š§šŗššæšš¾šš½š¾š š£šššš šŖš¾šššš¾šš š”šššš š„³ š„³ š„³
            """
            await c.send_message(m.chat.id, text)
            
        else:
            await c.send_message(m.chat.id, f"<code>š­ š“šššššš šÆšŗšš š§šŗšššš š”ššššš ! </code>\nā¢ š®šššš š»šššššš¾š šš¼šš /cancel komutunu kullanabilirsiniz āš»")
    else:
        await m.reply(f"š­ š¦ššš»ššŗ šš šŗšš½šŗ šŗššššæ š»šš šššš ššš !\nā¢ šøš¾šš šššš š»šŗšššŗšššŗš šš¼šš /game komutunu kullanabilirsiniz āš»")
