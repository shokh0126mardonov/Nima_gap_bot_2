from telegram.ext import (
    Updater,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    Filters
    )

from config import TOKEN
from config import LANGUAGE,NAME,GENDER,LOCATION,NUMBER
from handlers.cancel import cancel
from handlers.start import start
from handlers.register import set_name,set_gender,set_location,set_contact,start_register

def main()->None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    
    #Commandhandler
    dispatcher.add_handler(CommandHandler('start', start))
    
    conv_handler = ConversationHandler(
                    entry_points = [MessageHandler(Filters.regex("^(Ro'yxatdan o'tish|Registration)$"),start_register)],
                    states={
                        
                    NAME:[MessageHandler(Filters.text,set_name)],
                    GENDER:[MessageHandler(Filters.text,set_gender)],
                    LOCATION:[MessageHandler(Filters.location,set_location)],
                    NUMBER:[MessageHandler(Filters.contact,set_contact)],
                    
                    },
                    fallbacks=[CommandHandler('cancel', cancel)],
            )
    dispatcher.add_handler(conv_handler)
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()    