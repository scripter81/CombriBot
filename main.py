# - *- coding: utf- 8 - *-
from telegram.ext import Updater, CommandHandler

def start(bot, update):
  update.message.reply_text("Digita /aiuto per ottenere la lista dei comandi disponibili.")

def aiuto(bot, update):
  update.message.reply_text("sdsfd")
  
def regole(bot, update):
  update.message.reply_text("werwer")

def main():
  # Create Updater object and attach dispatcher to it
  updater = Updater('XXXX')
  dispatcher = updater.dispatcher
  print("Bot started")

  # Add command handler to dispatcher
  start_handler = CommandHandler('start',start)
  dispatcher.add_handler(start_handler)
  
  aiuto_handler = CommandHandler('aiuto',aiuto)
  dispatcher.add_handler(aiuto_handler)
  
  
  regole_handler = CommandHandler('regole',regole)
  dispatcher.add_handler(regole_handler)

  # Start the bot
  updater.start_polling()

  # Run the bot until you press Ctrl-C
  updater.idle()

if __name__ == '__main__':
  main()