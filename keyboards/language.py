from telegram import ReplyKeyboardMarkup,KeyboardButton

def get_language_keyboard()->ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton("Uzbek"),KeyboardButton("English")]
    ]
    
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        one_time_keyboard=True,
        resize_keyboard=True
    )