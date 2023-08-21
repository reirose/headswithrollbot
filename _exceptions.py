from telegram import Update
from telegram.ext import ContextTypes


async def input_error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mes = update.message
    await mes.reply_text(text="<b>Wrong input, try again.</b>\n\n<i>If you are confused, use /help</i>",
                         parse_mode="HTML")
