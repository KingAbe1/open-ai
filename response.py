from datetime import datetime
from pyChatGPT import ChatGPT
import constatnts as constatnt


def chat_gpt_3_reponse(input_text, update: None):
    user_message = str(input_text).lower()

    word_count = len(user_message.split())

    if (word_count < 3):
        return 'Please number of word in your sentence must be greater than two'
    else:
        update.message.reply_text(
            f'Please wait for the AI to prepare an answer to this question: {user_message}')
        api = ChatGPT(constatnt.SESSION)

        reply = api.send_message(f"{user_message}")

        return reply['message']
