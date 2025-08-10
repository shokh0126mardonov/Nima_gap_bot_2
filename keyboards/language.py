from telegram import(
    ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
    )


def get_language_markup()->InlineKeyboardMarkup:
    
    inline_keyboard = [
        [
        InlineKeyboardButton("Uzbek",callback_data='lang:uz'),
        InlineKeyboardButton("English",callback_data='lang:en')
        ]
    ]
    
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard) 

def get_register_markup()->InlineKeyboardMarkup:
    
    keyboard = [
        [
        KeyboardButton("Ro'yxatdan o'tish"),
        KeyboardButton("Bosh sahifa")
        ]
    ]
    
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        one_time_keyboard=True,
        resize_keyboard=True
        ) 