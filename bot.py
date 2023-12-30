from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel

API_ID = '25618507'
API_HASH = 'b8b91983b578360ec05a7e88e17b06ea'
SOURCE_CHANNEL_ID = -1001666241790
DESTINATION_CHANNEL_ID = -1002117307978

def move_messages(client):
    source_channel = InputPeerChannel(SOURCE_CHANNEL_ID)
    messages = client.iter_messages(source_channel, limit=100)

    for message in messages:
        client.forward_messages(DESTINATION_CHANNEL_ID, message)

def main():
    client = TelegramClient(None, API_ID, API_HASH)  # No session name

    client.connect()
    client.sign_in(bot_token='6876062883:AAFBonyQGtK_DmnQyEcnE1g40tLTF-Tn3K4')

    move_messages(client)

    client.disconnect()

if __name__ == '__main__':
    main()
