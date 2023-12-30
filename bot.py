from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistory, ForwardMessages

# Replace 'API_ID', 'API_HASH', 'SOURCE_CHANNEL_ID', and 'DESTINATION_CHANNEL_ID' with your actual values
API_ID = '25618507'
API_HASH = 'b8b91983b578360ec05a7e88e17b06ea'
SOURCE_CHANNEL_ID = -1001666241790
DESTINATION_CHANNEL_ID = -1002117307978

def move_messages(client):
    # Fetch messages in batches of 100
    messages = client.invoke(GetHistory(SOURCE_CHANNEL_ID, 0, 0, 100, 0, 0, 0)).messages

    # Forward each message to the destination channel
    for message in messages:
        client.invoke(ForwardMessages(DESTINATION_CHANNEL_ID, [message.id]))

    # If there are more messages, schedule the next batch
    if messages and len(messages) == 100:
        move_messages(client)

def main():
    # Create a Telethon client
    client = TelegramClient('1BVtsOK4Bu3yCEz9R9Uo6XBM4sWqYpi2o0HpvRmLS_UkH7lkaIlwx-bDHrYaYj11Cii5_QkZXuBgutr2FIomkVxgmDQLPihse8_PnsrAR28XTCKn21WXSpmwrOdlWMa_z9ehGQUnGvuRQvMKEd4-fH4Lb_iuw6WadAwMenB5tGv1iY8sSK7acBGlOMbZmW5ORpEG3TtHWtDSq4rNxKvH9NIs1YikjBuRn5SeBDRPDApTiE_Srwq5nEGfX00-51J4UUX-seqrs_0lP1oDjFuU7QryeVL5XkRg7saAh5UWctcTvSSY9EI-KbD1A0MWjz6z8FF5BkxbHpHjmsHvG0vZkYUWQYfTnnag=', API_ID, API_HASH)

    # Connect to the Telegram server
    client.connect()

    # Log in (you don't need to provide a phone number for a bot)
    client.sign_in(bot_token='6876062883:AAFBonyQGtK_DmnQyEcnE1g40tLTF-Tn3K4')

    # Fetch and forward messages
    move_messages(client)

    # Disconnect the client
    client.disconnect()

if __name__ == '__main__':
    main()
