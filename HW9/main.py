from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import view, TTTgame as t_g

app = ApplicationBuilder().token("5780078252:AAHdccUtESvBwB0-q-n82zY2WfhZhsFckRU").build()



app.add_handler(CommandHandler("start", view.start))
app.add_handler(CommandHandler("help", view.help))
app.add_handler(CommandHandler("play", t_g.game))
app.add_handler(MessageHandler(filters.TEXT, t_g.player_1))
app.run_polling(drop_pending_updates=True)

