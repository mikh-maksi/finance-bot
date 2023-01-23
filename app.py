from telegram.ext import Application, MessageHandler, filters, CommandHandler
account = 0

async def income(update, context):
    global account
    string_in = update.message.text
    elements = string_in.split(' ')
    account = account + int(elements[1])
    print(str(account))
    string_out = str(account)
    await update.message.reply_text(string_out)

async def echo(update, context):
    string_in = update.message.text

    if string_in == '/start':
        string_out = 'Hello! This is own finances bot!'
    else:
        string_out = string_in

    await update.message.reply_text(string_out)

application = Application.builder().token("2034824924:AAFc0q0PYPezeZ6G5kE10uBWhWSurKks-8A").build()

application.add_handler(CommandHandler('income', income))
application.add_handler(MessageHandler(filters.TEXT, echo))

application.run_polling()