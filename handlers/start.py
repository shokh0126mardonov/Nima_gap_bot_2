from telegram import Update
from telegram.ext import CallbackContext
from keyboards.language import get_language_keyboard

def start(update: Update, context: CallbackContext):
    user = update.effective_user.full_name
    update.message.reply_html(
        text=f"Assalomu alekum <b>{user}</b>!"
    )
    
    update.message.reply_html(
        text = 'Tilni tanlang / Select language',
        reply_markup=get_language_keyboard()
    )