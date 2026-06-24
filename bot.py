from telegram import Bot
import time

TOKEN = "8838024225:AAGvxHEpnML1YIXh4feTJWyU79rZwWGVYE0"
GROUP_ID = "@Avto_xabarchiuzBot"

bot = Bot(token=TOKEN)

message = "📢 Reklama: Bizning kanalga obuna bo‘ling!"

while True:
    try:
        bot.send_message(chat_id=GROUP_ID, text=message)
        print("Yuborildi")
    except Exception as e:
        print("Xatolik:", e)

    time.sleep(600)  # 10 minut
