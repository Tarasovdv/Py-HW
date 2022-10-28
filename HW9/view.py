from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}\n\
         это бот для игры в крестики нолики, набери /help чтобы узнать правила, или введи любой текст чтобы начать чтобы начать')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}\n\
       ЭЭЭЭ.')