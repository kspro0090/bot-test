from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import jdatetime

TOKEN = "7735006835:AAG5BwUxxA7SvXABioUKnYRbYf0gxtVFwrU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    today = jdatetime.date.today().strftime("%Y/%m/%d")
    await update.message.reply_text(f"سلام! امروز {today} است.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
