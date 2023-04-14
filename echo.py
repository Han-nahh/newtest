from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

##TOKEN = os.environ.get("5814904336:AAG1dikS2jVjgcpyQ2xC_Y-d1OBHGj4UAdU")
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def register_handlers(dispatcher):
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

def main():
    updater = Updater(token='5814904336:AAG1dikS2jVjgcpyQ2xC_Y-d1OBHGj4UAdU', use_context=True)
    dispatcher = updater.dispatcher

    register_handlers(dispatcher)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()