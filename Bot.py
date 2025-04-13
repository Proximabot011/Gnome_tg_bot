import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Twój token
TOKEN = '7753347523:AAFRETohFvuWsV9FCLvc_m9GKEJHQ95mgvY'

# Funkcja startowa
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Witaj! Jestem Twoim botem.')

# Funkcja komendy /help
def help_command(update: Update, context: CallbackContext):
    update.message.reply_text('Dostępne komendy:\n/start - Uruchamia bota\n/help - Wyświetla pomoc')

def main():
    # Ustawienia logowania
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Inicjalizacja Updatera
    updater = Updater(TOKEN)

    # Dispatcher do obsługi komend
    dispatcher = updater.dispatcher

    # Dodanie handlerów komend
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Uruchomienie bota
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
