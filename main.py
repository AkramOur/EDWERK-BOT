from telegram.ext import *
import Responses as rp
import Constantes as keys


print("Bot Started")

def start_command(update, context):
    update.message.reply_text('Type something random to get started!')

def help_command(update, context):
    update.message.reply_text('If you need help!')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = rp.simple_response(text)
    update.message.reply_text(response)

def recetteAddress_command(update, context):
    update.message.reply_text(rp.addressIp_command())


def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY,use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(CommandHandler("recette",recetteAddress_command))

    dp.add_handler(MessageHandler(Filters.text,handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
