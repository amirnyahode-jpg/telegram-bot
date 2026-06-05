import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.environ.get("8996322599:AAFQckLcxpSuK75k_nxQqqQ0pX8APUm60jE")
ADMIN_ID = os.environ.get("8688294225")

# ---------- MAIN MENU ----------
def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🛒 خرید", callback_data="buy")],
        [InlineKeyboardButton("🧑‍💻 پشتیبانی", callback_data="support")]
    ])

# ---------- START ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "به ربات خوش آمدید 👇",
        reply_markup=main_menu()
    )

# ---------- BUTTONS ----------
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()

    # پشتیبانی
    if q.data == "support":
        context.user_data["support_mode"] = True
        await q.message.reply_text(
            "لطفا پیام خود را همینجا ارسال کنید ❤️‍🔥\nبا تشکر 🌹🌹"
        )

    # خرید منو
    elif q.data == "buy":
        await q.message.reply_text(
            "یکی از پکیج‌ها را انتخاب کنید:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("5 گیگ - 80 هزار", callback_data="5g")],
                [InlineKeyboardButton("10 گیگ - 120 هزار", callback_data="10g")],
                [InlineKeyboardButton("20 گیگ - 200 هزار", callback_data="20g")],
                [InlineKeyboardButton("🔙 بازگشت", callback_data="back")]
            ])
        )

    elif q.data == "back":
        await q.message.reply_text("منوی اصلی 👇", reply_markup=main_menu())

    # پکیج‌ها
    elif q.data == "5g":
        await q.message.reply_text(
            "💰 مبلغ ۸۰ هزار تومان به شماره کارت زیر به نام امیررضا هژبر را واریز کنید:\n\n"
            "6104338644728640"
            "بعد از پرداخت رسید را ارسال کنید 🌹"
        )

    elif q.data == "10g":
        await q.message.reply_text(
            "💰 مبلغ ۱۲۰ هزار تومان شماره کارت زیر به نام امیررضا هژبر را واریز کنید:\n\n"
            "6104338644728640"
            "بعد از پرداخت رسید را ارسال کنید 🌹"
        )

    elif q.data == "20g":
        await q.message.reply_text(
            "💰 مبلغ ۲۰۰ هزار تومان شماره کارت زیر به نام امیررضا هژبر را واریز کنید:\n\n"
            "6104338644728640"
            "بعد از پرداخت رسید را ارسال کنید 🌹"
        )

# ---------- SUPPORT + RECEIPT HANDLER ----------
async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # پشتیبانی
    if context.user_data.get("support_mode"):
        context.user_data["support_mode"] = False

        await update.message.reply_text(
            "پیام شما ارسال شد 🌹\nبا تشکر ❤️‍🔥"
        )

        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"📩 پیام پشتیبانی:\n\n{update.message.text}"
        )

    # رسید (عکس)
    elif update.message.photo:
        await update.message.reply_text(
            "🌹 با تشکر از اعتماد شما 🌹\n"
            "رسید در حال بررسی است...\n"
            "کمتر از ۲۰ دقیقه آینده فعال می‌شود ❤️‍🔥"
        )

        await context.bot.send_photo(
            chat_id=ADMIN_ID,
            photo=update.message.photo[-1].file_id,
            caption="📥 رسید جدید دریافت شد"
        )

# ---------- APP ----------
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.add_handler(MessageHandler(filters.TEXT | filters.PHOTO, text_handler))

app.run_polling()
