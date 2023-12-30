from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '6876062883:AAFBonyQGtK_DmnQyEcnE1g40tLTF-Tn3K4'

# Replace 'SOURCE_CHANNEL_ID' and 'DESTINATION_CHANNEL_ID' with your actual channel IDs
SOURCE_CHANNEL_ID = -1001666241790  # Example: -1001234567890
DESTINATION_CHANNEL_ID = -1002117307978  # Example: -100987654321

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bot is running.')

def move_messages(context: CallbackContext) -> None:
    # Fetch all messages from the source channel
    messages = context.bot.get_chat_history(chat_id=SOURCE_CHANNEL_ID, limit=100)

    # Forward each message to the destination channel
    for message in messages:
        context.bot.forward_message(chat_id=DESTINATION_CHANNEL_ID, from_chat_id=SOURCE_CHANNEL_ID, message_id=message.message_id)

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))

    # Use a job queue to periodically move messages from the source to the destination channel
    job_queue = updater.job_queue
    job_queue.run_repeating(move_messages, interval=3600, first=0)  # Adjust the interval as needed (3600 seconds = 1 hour)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop it
    updater.idle()

if __name__ == '__main__':
    main()
