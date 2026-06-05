from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters

TOKEN = "8996322599:AAFQckLcxpSuK75k_nxQqqQ0pX8APUm60jE"
ADMIN_ID = "8688294225"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛒 خرید", callback_data="buy")],
        [InlineKeyboardButton("🧑‍💻 پشتیبانی", callback_data="support")]
    ]
    await update.message.reply_text("خوش آمدی 👇", reply_markup=InlineKeyboardMarkup(keyboard))

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()

    if q.data == "support":
        await q.message.reply_text(f"پشتیبانی: {ADMIN_ID}")

    elif q.data == "buy":
        keyboard = [
            [InlineKeyboardButton("پکیج 1", callback_data="p1")],
            [InlineKeyboardButton("🔙 بازگشت", callback_data="back")]
        ]
        await q.message.reply_text("انتخاب کن:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif q.data == "back":
        await start(update, context)

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
