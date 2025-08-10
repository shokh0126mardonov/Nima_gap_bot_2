from telegram import Update,ReplyKeyboardMarkup,KeyboardButton
from telegram.ext import CallbackContext,ConversationHandler
from config import LANGUAGE,NAME,GENDER,LOCATION,NUMBER
#set_language,set_name,set_gender,set_location,set_contact


def start_register(update:Update,context:CallbackContext):
    update.message.reply_text("Ro'yxatdan o'tish uchun quyidagi malumotlaringizni yuboring")
    update.message.reply_text("Name yuboring")
    return NAME


def set_name(update:Update,context:CallbackContext):
    
    name = update.message.text
    context.user_data['name'] = name
    
    update.message.reply_text("Name qabulq qilindi")
    update.message.reply_text("Gender yuboring",reply_markup=ReplyKeyboardMarkup(
        [
            [KeyboardButton('Erkak'),KeyboardButton("Ayol")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))
    
    return GENDER

def set_gender(update:Update,context:CallbackContext):
    
    gender = update.message.text
    context.user_data['gender'] = gender
    
    update.message.reply_text("Gender qabul qilindi")
    update.message.reply_text("Location yuboring",reply_markup=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("Location",request_location = True)]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))
    return LOCATION

def set_location(update:Update,context:CallbackContext):
    
    location = update.message.location
    context.user_data['location'] = {
        "longitude":location.longitude,
        "latitude":location.latitude
    }
    
    update.message.reply_text("Location qabul qilindi")
    update.message.reply_text("Contact yuboring",reply_markup=ReplyKeyboardMarkup(
        [
            [KeyboardButton("Contact yuborish",request_contact=True)],
            
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))
    return NUMBER

def set_contact(update:Update,context:CallbackContext):
    
    contact = update.message.contact.phone_number
    context.user_data['contact'] = contact
    
    print(context.user_data)
    
    update.message.reply_text("Contact qabul qilindi")
    update.message.reply_text("Siz registratsiya qilindizngiz!")
    return ConversationHandler.END
