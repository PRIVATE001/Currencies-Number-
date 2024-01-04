import requests
import telebot
from datetime import datetime
from dotenv import dotenv_values



config = dotenv_values(".env")

token = "Token"
bot = telebot.TeleBot(token)

def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_price = response["btc_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")

def telegram_bot(token):
    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id,"""
↯︙ مرحباً  بك عزيزي في بوت سعر البتكوين الان ارسل (price) لإظهار سعر اليوم [🔖] 
---------------------------------  
Welcome Dear To The Bitcoin Price Bot Now Send (price) To Show Today's Price [📬] 
""")
    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "price":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = req.json()
                sell_price = response["btc_usd"]["sell"]
                print(f"""{datetime.now().strftime('%Y-%m-%d %H:%M')}
Sell BTC price :- {sell_price}
""")
                bot.send_message(
                    message.chat.id,
                    f"""{datetime.now().strftime('%Y-%m-%d %H:%M')}
Sell BTC price :- {sell_price}
""")
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "حسنًا...ولكن ليس بعد ذلك."
                )
        else:
            bot.send_message(
                    message.chat.id,
                    "لم تطلب...تحقق من الأمر !"
            )

    bot.polling()


if __name__ == "__main__":
    telegram_bot(token)