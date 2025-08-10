from telegram.ext import CallbackContext
from telegram import Update
from keyboards import get_language_markup,get_register_markup
from config.states import LANGUAGE

def start(update:Update,context:CallbackContext):
    full_name = update.effective_user.full_name
    
    text = f"Assalomu alekum {full_name} \nSiz Nima gap suhbat botiga xush kelibsiz!"
    
    update.message.reply_text(
        text=text
    )
    
    update.message.reply_text(
        text="Tilni tanlang/Select language",
        reply_markup=get_language_markup()
    )
    
    update.message.reply_text(
        text="Ro'yxatdan o'tish",
        reply_markup = get_register_markup()
    )
    
    return LANGUAGE