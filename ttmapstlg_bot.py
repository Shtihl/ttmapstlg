import asyncio
import config
import asyncpraw
from aiogram import Bot, types

token = config.TOKEN
chat_id = config.CHAT_ID
reddit_client = config.REDDIT_CLIENT_ID
reddit_secret = config.REDDIT_SECRET

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
reddit = asyncpraw.Reddit(
    client_id=reddit_client,
    client_secret=reddit_secret,
    user_agent="random_reddit_bot/0.0.1",
)
maps = []
timeout = 30
subreddit_name = "battlemaps"
post_limit = 5


async def send_message(channel_id: int, text: str):
    await bot.send_message(channel_id, text)


async def main():
    while True:
        await asyncio.sleep(timeout)
        maps_submissions = await reddit.subreddit(subreddit_name)
        maps_submissions = maps_submissions.new(limit=post_limit)
        item = await maps_submissions.__anext__()
        if item.title not in maps:
            maps.append(item.title)
            await send_message(chat_id, item.url)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
