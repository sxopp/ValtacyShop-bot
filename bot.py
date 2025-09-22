from telegram.ext import Updater, CommandHandler
import os

# get token from environment variable (you will set this in Render later)
TOKEN = os.getenv("BOT_TOKEN")

# example key pool
keys = ["KEY-0001", "KEY-0002", "KEY-0003"]

def start(update, context):
    update.message.reply_text("👋 Welcome! Type /buy to purchase a key.")

def buy(update, context):
    update.message.reply_text(
        "💳 Please send ₱50 to GCash 09654050564\n"
        "After payment, press /done"
    )

def done(update, context):
    global keys
    if keys:
        key = keys.pop(0)  # give first unused key
        update.message.reply_text(f"✅ Payment confirmed!\nHere is your key:\n{key}")
    else:
        update.message.reply_text("❌ Sorry, no keys left!")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("buy", buy))
dp.add_handler(CommandHandler("done", done))

updater.start_polling()
updater.idle()
