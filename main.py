import json
import telebot
from prices import price

"""Telegram chat bot to send crypto currency prices collected from coinmarketcap.com API 
to chat group at a scheduled time per day, once per day . Will be set as a cron job on server."""

print("BOT RUNNING...")


with open("./json/chat_ids.json", "r") as chat_ids:  # chat group id from json file
    CHAT_ID = json.load(chat_ids)

with open(
    "./json/bot_api_key.json", "r"
) as bot_api_key:  # loads bot api key from json file
    TOKEN = json.load(bot_api_key)

bot = telebot.TeleBot(
    TOKEN.get("bot_api_key"), parse_mode=None
)  # connects to telegram api


def send_coin_message(coin):
    bot.send_message(CHAT_ID.get("chat_group"), price(coin=coin, currency="GBP"))


def message_loop():
    """Add or delete coins from this list to add or remove from messages"""
    coinlist = ["DOGE", "BONK", "ADA"]

    for coin in coinlist:
        send_coin_message(coin)


def send_final_message():
    """This function stops bot polling once messages are sent"""
    bot.send_message(
        CHAT_ID.get("chat_group"), "Bot shutting down . Goodbye, Dominar !"
    ),
    bot.stop_polling()
    print("BOT TIMED SLEEP.\nBOT STOPPED")


@bot.message_handler(commands=["start"])
def send_welcome(message):
    """These commands only used initial when setting up or testing. Bot is only meant to send automated messages"""
    bot.reply_to(message, "Its great to be awake, my liege.")


@bot.message_handler(commands=["check"])
def send_confirmation(message):
    """These commands only used initial when setting up or testing. Bot is only meant to send automated messages"""
    bot.reply_to(message, "I am still here, my liege.")


@bot.message_handler(commands=["sleep"])
def kill_command(message):
    """These commands only used initial when setting up or testing. Bot is only meant to send automated messages"""
    bot.reply_to(message, "Ill sleep immediately , my liege")
    bot.stop_polling()
    print("BOT PROCESS KILLED BY USER.\nBOT STOPPED")


def runbot():

    message_loop()
    send_final_message()


"""Uncomment this when used on AWS"""
# def lambda_handler(event=None, context=None): # This needed for AWS lambda
#     runbot()

if __name__ == "__main__":
    runbot()  # comment out/delete when on AWS
    # lambda_handler() # only have this func here on AWS
    bot.infinity_polling()  # stays connected to Telegram API
