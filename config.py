from os import environ
from dotenv import load_dotenv

load_dotenv()

TOKEN = environ.get("TOKEN")
CHAT_ID = environ.get("CHAT_ID")
REDDIT_CLIENT_ID = environ.get("REDDIT_CLIENT_ID")
REDDIT_SECRET = environ.get("REDDIT_SECRET")
