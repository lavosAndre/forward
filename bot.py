from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import time

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '6876062883:AAFBonyQGtK_DmnQyEcnE1g40tLTF-Tn3K4'

# Replace 'SOURCE_CHANNEL_ID' and 'DESTINATION_CHANNEL_ID' with your actual channel IDs
SOURCE_CHANNEL_ID = -1001666241790
DESTINATION_CHANNEL_ID = -1002117307978

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bot is running.')

def move_messages(context: CallbackContext, last_message_id=None) -> None:
    # Fetch messages in batches of 100
    messages = context.bot.get_chat_history(chat_id=SOURCE_CHANNEL_ID, limit=100, offset_id=last_message_id)

    # Forward each message to the destination channel
    for message in messages:
        context.bot.forward_message(chat_id=DESTINATION_CHANNEL_ID, from_chat_id=SOURCE_CHANNEL_ID, message_id=message.message_id)

    # If there are more messages, schedule the next batch
    if messages and len(messages) == 100:
        last_message_id = messages[-1].message_id
        context.job_queue.run_once(lambda c: move_messages(c, last_message_id), when=2)  # Wait 2 seconds before the next batch

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))

    # Schedule the initial move_messages call
    updater.job_queue.run_once(move_messages, when=0)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop it
    updater.idle()

if __name__ == '__main__':
    main()
