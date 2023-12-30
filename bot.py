from telethon.sync import TelegramClient

API_ID = '25618507'
API_HASH = 'b8b91983b578360ec05a7e88e17b06ea'
SOURCE_CHANNEL_ID = -1001666241790

client = TelegramClient(None, API_ID, API_HASH)  # No session name
client.connect()

source_channel = client.get_entity(SOURCE_CHANNEL_ID)
print("Source Channel Access Hash:", source_channel.access_hash)

client.disconnect()
