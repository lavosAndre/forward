from telethon.telegram_bare_client import TelegramBareClient

API_ID = '25618507'
API_HASH = 'b8b91983b578360ec05a7e88e17b06ea'
SOURCE_CHANNEL_ID = -1001666241790
DESTINATION_CHANNEL_ID = -1002117307978

async def move_messages(client):
    async for message in client.iter_messages(SOURCE_CHANNEL_ID, limit=100):
        await client.send_message(DESTINATION_CHANNEL_ID, message)

async def main():
    async with TelegramBareClient('anon', API_ID, API_HASH) as client:
        await client.connect()
        await client.sign_in(bot_token='6876062883:AAFBonyQGtK_DmnQyEcnE1g40tLTF-Tn3K4')

        await move_messages(client)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
