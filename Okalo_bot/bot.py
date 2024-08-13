from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import logging

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Функция для команды /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привет! Я бот центра помощи жертвам насилия. Используйте /help для получения списка команд.')

# Функция для команды /help
async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Список доступных команд:\n/start - Начать общение\n/help - Список команд\n/info - Получить информацию о центре помощи\n/contacts - Контактные данные')

# Функция для команды /info
async def info(update: Update, context: CallbackContext) -> None:
    info_text = """
    Центр помощи жертвам насилия "Okolo" предоставляет различные услуги поддержки, включая:
    - Психологическая помощь
    - Юридическая консультация
    - Временное жилье
    - Социальная помощь

    Наша миссия - поддерживать и защищать жертв насилия, предоставляя необходимые ресурсы и поддержку.
    """
    await update.message.reply_text(info_text)

# Функция для команды /contacts
async def contacts(update: Update, context: CallbackContext) -> None:
    contacts_text = """
    Контактные данные центра помощи жертвам насилия "Okolo":
    - Телефон: +123456789
    - Email: help@okolo.org
    - Адрес: ул. Примерная, д. 1, г. Москва
    """
    await update.message.reply_text(contacts_text)

def main() -> None:
    # Вставьте сюда ваш токен
    application = Application.builder().token("7183071193:AAFKtG86Pn02QjumdF4AmF6jMt9RF1CtV40").build()

    # Обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("contacts", contacts))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
