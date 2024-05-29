import logging
import json

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
from filestore import FileStore

from openai import OpenAI

with open('config.json') as config_file:
    config = json.load(config_file)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

client = OpenAI(api_key=config.get('OPENAI_API_KEY'))
store = FileStore()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text(f"Zo Zo {user.first_name}!")

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    thread_id = store.fetch(update.effective_user.id)
    if not thread_id:
        thread = client.beta.threads.create()
        store.add(update.effective_user.id, thread.id)
        thread_id = thread.id

    thread_message = client.beta.threads.messages.create(
        thread_id,
        role="user",
        content=update.message.text,
    )
    stream = client.beta.threads.create_and_run(
        assistant_id=config.get("ASSISTANT_ID"),
        thread={"messages": [{"role": "user", "content": update.message.text}]}, stream=True
    )
    response = "💀"
    try:
        for event in stream:
            if event.event == "thread.message.completed":
                response = event.data.content[0].text.value
    except Exception as e:
        print(e)
        pass
    await update.message.reply_text(response)


def main() -> None:
    application = Application.builder().token(config.get('TELEGRAM_TOKEN')).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()