from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # ... (тvoї повідомлення із кнопками)
    await update.message.reply_text("Привіт! Обери дію 👇", reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("📘 Безкоштовний гайд", callback_data="free_guide")],
        [InlineKeyboardButton("🔐 Повний курс", callback_data="full_course")],
    ]))

# ... (другий handler як раніше)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.run_polling()
