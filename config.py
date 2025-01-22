from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

class Config(object):
    # required config variables
    API_HASH = getenv("API_HASH", c950aa8fafd22287c3d4e9a344cb89ea)                # get from my.telegram.org
    API_ID = int(getenv("API_ID", 26481303))                  # get from my.telegram.org
    BOT_TOKEN = getenv("BOT_TOKEN", 7600815065:AAEUoui_9DCg8ppIJoegOwbZARfDKBjL-i0)              # get from @BotFather
    DATABASE_URL = getenv("DATABASE_URL", mongodb+srv://SiestaXMusic:BGMI272@cluster0.nik6j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0)        # from https://cloud.mongodb.com/
    HELLBOT_SESSION = getenv("HELLBOT_SESSION", BAGUEpcApxQXPsSs1E6uIdDSQNRcvo9Gd99m9vKesiA9hBdrFndpryr7HpsCZBPiNYSLqzV_ACEHCpsqjwl9f3H6h-vA09Ht7pGZhwaNx7VpKBYx68_msitvFiRLVIM4eEmt4UVkZ_qlgG-4-co0N0peZcaYVqJUFwc9TjxuKJw8bAJLFyc_fuCRsit7XX6FGiSM3it0dx2tuJkAW3LpHBm5VhIt07JeKYdxZ8pfIdbs0xBZ6RyZAIagb9lOwge5xr73xncvM3eTOc_5L1JYhpoOQ6FPGrpFbc0Z57igOsAt5KxgrNpFavpfw8shQc7xHiLTe81uM2UWFhqUhj-gS23CMe-MxAAAAAHSItAjAA)  # enter your session string here
    LOGGER_ID = int(getenv("LOGGER_ID", -1002239560457))            # make a channel and get its ID
    OWNER_ID = getenv("OWNER_ID", "7593550190")                  # enter your id here

    # optional config variables
    BLACK_IMG = getenv("BLACK_IMG", "https://telegra.ph/file/2c546060b20dfd7c1ff2d.jpg")        # black image for progress
    BOT_NAME = getenv("BOT_NAME", "@SiestaXMusiccBot")   # dont put fancy texts here.
    BOT_PIC = getenv("BOT_PIC", "https://drive.google.com/file/d/1GFvDlUen6oxhI_yGFuZRCmDEa8fhnf8z/view?usp=drivesdk")           # put direct link to image here
    LEADERBOARD_TIME = getenv("LEADERBOARD_TIME", "3:00")   # time in 24hr format for leaderboard broadcast
    LYRICS_API = getenv("LYRICS_API", None)             # from https://docs.genius.com/
    MAX_FAVORITES = int(getenv("MAX_FAVORITES", 30))    # max number of favorite tracks
    PLAY_LIMIT = int(getenv("PLAY_LIMIT", 0))           # time in minutes. 0 for no limit
    PRIVATE_MODE = getenv("PRIVATE_MODE", "off")        # "on" or "off" to enable/disable private mode
    SONG_LIMIT = int(getenv("SONG_LIMIT", 0))           # time in minutes. 0 for no limit
    TELEGRAM_IMG = getenv("TELEGRAM_IMG", None)         # put direct link to image here
    TG_AUDIO_SIZE_LIMIT = int(getenv("TG_AUDIO_SIZE_LIMIT", 104857600))     # size in bytes. 0 for no limit
    TG_VIDEO_SIZE_LIMIT = int(getenv("TG_VIDEO_SIZE_LIMIT", 1073741824))    # size in bytes. 0 for no limit
    TZ = getenv("TZ", "Asia/Kolkata")   # https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

    # do not edit these variables
    BANNED_USERS = filters.user()
    CACHE = {}
    CACHE_DIR = "./cache/"
    DELETE_DICT = {}
    DWL_DIR = "./downloads/"
    GOD_USERS = filters.user()
    PLAYER_CACHE = {}
    QUEUE_CACHE =  {}
    SONG_CACHE = {}
    SUDO_USERS = filters.user()


# get all config variables in a list
all_vars = [i for i in Config.__dict__.keys() if not i.startswith("__")]
