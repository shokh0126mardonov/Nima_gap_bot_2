from config.config import TOKEN
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler
    )
from handlers.start import start


def main()->None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    
    # Commandhandler
    dispatcher.add_handler(CommandHandler("start",start))
    
    #MessageHandler
    
    updater.start_polling()
    updater.idle()
    
if __name__ == "__main__":
    main()