
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from helper.database import db
from config import Config, Txt  
  

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await db.add_user(client, message)                
    button = InlineKeyboardMarkup([[
        InlineKeyboardButton("🔺 𝑼𝑷𝑫𝑨𝑻𝑬 𝑪𝑯𝑨𝑵𝑵𝑬𝑳 🔺", url="https://t.me/RedOfficiall")
        ],[
        InlineKeyboardButton("☕ 𝑩𝑼𝒀 𝑴𝑬 𝑪𝑶𝑭𝑭𝑬𝑬 ☕", url='https://p.paytm.me/xCTH/vo37hii9'),
        InlineKeyboardButton("𝑴𝑶𝑽𝑰𝑬𝑺 𝑮𝑹𝑶𝑼𝑷", url='https://t.me/RedMovies1')
        ],[
        InlineKeyboardButton("🦋 𝑪𝑶𝑵𝑻𝑨𝑪𝑻 🦋", url='https://telegram.me/MR_DINNO1'),
        InlineKeyboardButton('🛠️ 𝑯𝑬𝑳𝑷', callback_data='help')
    ]])
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.START_TXT.format(user.mention), reply_markup=button)       
    else:
        await message.reply_text(text=Txt.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)
   

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=Txt.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup([[
                InlineKeyboardButton("🔺 𝑼𝑷𝑫𝑨𝑻𝑬 𝑪𝑯𝑨𝑵𝑵𝑬𝑳 🔺", url="https://t.me/RedOfficiall")
                ],[
                InlineKeyboardButton("☕ 𝑩𝑼𝒀 𝑴𝑬 𝑪𝑶𝑭𝑭𝑬𝑬 ☕", url='https://p.paytm.me/xCTH/vo37hii9'),
                InlineKeyboardButton("𝑴𝑶𝑽𝑰𝑬𝑺 𝑮𝑹𝑶𝑼𝑷", url='https://t.me/RedMovies1')
                ],[
                InlineKeyboardButton("🦋 𝑪𝑶𝑵𝑻𝑨𝑪𝑻 🦋", url='https://telegram.me/MR_DINNO1'),
                InlineKeyboardButton('🛠️ 𝑯𝑬𝑳𝑷', callback_data='help')
            ]])
        )
    elif data == "help":
        await query.message.edit_text(
            text=Txt.HELP_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
            ]])            
        )
    elif data == "abot":
        await query.message.edit_text(
            text=Txt.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("❣️ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")
                ],[
                InlineKeyboardButton("🖥️ Hᴏᴡ Tᴏ Mᴀᴋᴇ", url="https://youtu.be/GfulqsSnTv4")
                ],[
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
            ]])            
        )
    elif data == "dv":
        await query.message.edit_text(
            text=Txt.DEV_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("❣️ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")
                ],[
                InlineKeyboardButton("🖥️ Hᴏᴡ Tᴏ Mᴀᴋᴇ", url="https://youtu.be/GfulqsSnTv4")
                ],[
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
            ]])          
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()
