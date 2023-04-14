from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
from telegram import Update, Bot
import os
from typing import Optional

TOKEN = os.environ.get("TOKEN")
from fastapi import FastAPI,Request
from pydantic import BaseModel

app = FastAPI()
class TelegramWebhook(BaseModel):
    '''
    Telegram Webhook Model using Pydantic for request body validation
    '''
    update_id: int
    message: Optional[dict]
    edited_message: Optional[dict]
    channel_post: Optional[dict]
    edited_channel_post: Optional[dict]
    inline_query: Optional[dict]
    chosen_inline_result: Optional[dict]
    callback_query: Optional[dict]
    shipping_query: Optional[dict]
    pre_checkout_query: Optional[dict]
    poll: Optional[dict]
    poll_answer: Optional[dict]

@app.get("/")
def index():
    return {"message": "Hello World"}


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def register_handlers(dispatcher):
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

@app.post("/webhook")
def webhook(webhook_data: TelegramWebhook):
    '''
    Telegram Webhook
    '''
    # Method 1
    bot = Bot(token=TOKEN)
    update = Update.de_json(webhook_data, app.bot)
    dispatcher = Dispatcher(bot, None, workers=4)
    register_handlers(dispatcher)

    # handle webhook request
    dispatcher.process_update(update)

    return {"message": "ok"}

@app.get("/")
def index():
    return {"message": "Hello World"}

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    register_handlers(dispatcher)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


