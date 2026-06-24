from telegram import Bot
import time

TOKEN = "YOUR_BOT_TOKEN"
GROUP_ID = "@your_group_username"

bot = Bot(token=TOKEN)

message = "📢 Reklama: Bizning kanalga obuna bo‘ling!"

while True:
    try:
        bot.send_message(chat_id=GROUP_ID, text=message)
        print("Yuborildi")
    except Exception as e:
        print("Xatolik:", e)

    time.sleep(600)  # 10 minut
