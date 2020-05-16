from telegram.ext import Updater, CommandHandler

def main():
    updater = Updater(token = "766224020:AAFpRgLT12Owcma4qq8oi0PxHGOroN_HYF0", use_context = True)

    updater.dispatcher.add_handler(CommandHandler("start", start))

    updater.dispatcher.add_handler(CommandHandler("repite", repite))

    updater.dispatcher.add_handler(CommandHandler("suma", suma))

    updater.start_polling()
    updater.idle()

def start(update, context):
    update.message.reply_text("hola soy un bot")

def repite(update, context):
    update.message.reply_text(update.message.text)

def suma(update, context):
    update.message.reply_text("el resultado es: "+ str(int(context.args[0])+ int(context.args[1])))
    
main()