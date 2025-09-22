import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

# Your GCash details
GCASH_NUMBER = "09654050564"
GCASH_NAME = "RE****D Y."

# Simple key stock
KEYS = ["ABC123", "XYZ456", "JKL789"]  # replace with your keys

# Track which keys were given
used_keys = []

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to ValtacyShop! ✅ Use /buy to purchase a key.")

# Buy command
async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        f"💳 Please pay using GCash:\n\n"
        f"📱 Number: {GCASH_NUMBER}\n"
        f"👤 Name: {GCASH_NAME}\n\n"
        f"After payment, send your screenshot here 📸.\n"
        f"An admin will verify and send your key."
    )
    await update.message.reply_text(message)

# Admin command to send key manually
async def sendkey(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != int(os.getenv("ADMIN_ID", "0")):
        await update.message.reply_text("🚫 You are not authorized to send keys.")
        return

    if not context.args:
        await update.message.reply_text("Usage: /sendkey <username>")
        return

    username = context.args[0]
    if len(KEYS) == 0:
        await update.message.reply_text("❌ No keys left in stock!")
        return

    key = KEYS.pop(0)
    used_keys.append(key)

    await update.message.reply_text(f"✅ Sent key {key} to @{username}")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("buy", buy))
    app.add_handler(CommandHandler("sendkey", sendkey))

    app.run_polling()

if __name__ == "__main__":
    main()
