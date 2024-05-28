from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = '7237664225:AAHSkAAjgz3mg_qBp4Vz80u9MxzKvLBPHys'
WEB_SERVER_URL = 'https://576c-103-129-215-67.ngrok-free.app'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    link = f"{WEB_SERVER_URL}/capture?user_id={user.id}"
    keyboard = [[InlineKeyboardButton("Capture Image and Location", url=link)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Click the button below to capture image and location.', reply_markup=reply_markup)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == '__main__':
    main()
