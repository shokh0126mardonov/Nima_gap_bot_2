def set_language(update:Update,context:CallbackContext):
    name = update.message.text
    context['name'] = name
    
    update.message.reply_text("Language qabul qilindi")
    update.message.reply_text("Name yuboring")
    return NAME