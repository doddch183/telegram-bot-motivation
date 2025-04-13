from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

# Мотиваційні повідомлення
motivations = [
    "Ти можеш більше, ніж думаєш.",
    "Кожен день — це нова можливість.",
    "Не здавайся. Найкраще ще попереду.",
    "Світ змінюється через твої дії.",
    "Сила — всередині тебе. Вір у себе."
]

# Функція /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Я бот мотивації. Напиши /motivate, щоб отримати пораду.")

# Функція /motivate
async def motivate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = random.choice(motivations)
    await update.message.reply_text(message)

# Основна функція
if __name__ == '__main__':
    app = ApplicationBuilder().token("8060030188:AAFt8XNpDcQEa7qH5gCgGor-GtydOX6sCQ8").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("motivate", motivate))

    print("Бот запущено!")
    app.run_polling()
