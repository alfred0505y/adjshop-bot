from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

products = {
    "Nike": "Кроссовки Nike - стильные и удобные.",
    "Adidas": "Кроссовки Adidas - качество и комфорт.",
    "Puma": "Кроссовки Puma - для спорта и отдыха."
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(name, callback_data=name)] for name in products.keys()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Выберите бренд:', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    brand = query.data
    await query.edit_message_text(text=products.get(brand, "Описание отсутствует."))

if __name__ == '__main__':
    app = ApplicationBuilder().token("7645541553:AAEr0S0iU5TJsKo547ebFJ_12ECKvaLOMog").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()
