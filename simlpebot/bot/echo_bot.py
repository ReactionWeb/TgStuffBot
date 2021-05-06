from telegram.ext import Updater
from telegram.ext import CommandHandler


def main() -> None:
    updater = Updater(token='1702231704:AAGA5EzQ9AbOIrjfVpzK0XDGBlkwnufj32M')
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    updater.start_polling()
    updater.idle()


def start_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def help_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="How can i help you, commander?")


if __name__ == '__main__':
    main()
