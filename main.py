import constatnts as keys
from telegram.ext import *
import response as res

print("BOT STARTED......")


def start_command(update, context):
    try:
        update.message.reply_text(
            'Please ask any kind questions that\'s on your mind')
    except:
        update.message.reply_text('Please try again after some time')


def help_command(update, context):
    try:
        update.message.reply_text(
            'If you need any kind of help please contact me in telegram by this username @k1ngAbe1 . I will try my best to reply to your message quickly.')
    except:
        update.message.reply_text('Please try again after some time')


def suggestion_command(update, context):
    try:
        update.message.reply_text(
            'If have any kind suggestion regarding the bot please contact me in telegram by this username @k1ngAbe1 . I will try my best to reply to your message quickly.')
    except:
        update.message.reply_text('Please try again after some time')


def complaint_command(update, context):
    try:
        update.message.reply_text(
            'If have any kind complaint regarding the bot please contact me in telegram by this username @k1ngAbe1 . I will try my best to reply to your message quickly.')
    except:
        update.message.reply_text('Please try again after some time')


def handle_message(update, context):
    try:
        text = str(update.message.text).lower()
        response = res.chat_gpt_3_reponse(text, update)

        update.message.reply_text(response)
    except:
        update.message.reply_text('Please try again after some time')


def error(update, context):
    try:
        update.message.reply_text(
            f'Sorry it seems there is a problem: {context.error}\nPlease try again after some time.')
    except:
        update.message.reply_text('Please try again after some time')


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("suggestion", suggestion_command))
    dp.add_handler(CommandHandler("complain", complaint_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
