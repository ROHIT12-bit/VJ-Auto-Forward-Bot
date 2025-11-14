from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "72095ec36984aa9ceb0dbaa9cec31559")
      API_ID = int(getenv("API_ID", "20366634"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "8318148315:AAFvlhMNP_X8BCdKkCnvqi8ehRQ4k98emrY")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001789825040:-1003199481893").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
