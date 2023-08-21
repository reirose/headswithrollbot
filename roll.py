from random import randint, seed
from re import match
from time import time

from telegram import Update
from telegram.ext import ContextTypes

from _exceptions import input_error

last_rolls: dict = {}


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mes = update.message
    text = ("Usage:\n<code>/roll [n]d[m]</code> -- roll <i>n</i> d<i>m</i> dices\n"
            "Available dices: d4, d6, d8, d10, d12, d20, d100\n"
            "E.g.: <code>/roll 3d6 1d20</code>\n\n"
            "<code>/reroll</code> -- reroll last dices\n\n"
            "<i>Note: just /roll will roll 1d100</i>")
    await mes.reply_text(text, parse_mode="HTML")


async def roll(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mes = update.message

    if not context.args:
        context.args = ['1d100']

    rolls: list = []
    total = 0

    for string in context.args:
        try:
            matched = match("([0-9]+)d([0-9]+)", string)
            k, d_type = matched.group(1), matched.group(2)

        except (IndexError, AttributeError):
            await input_error(update, context)
            return

        if d_type not in ['4', '6', '8', '10', '12', '20', '100']:
            await input_error(update, context)
            return

        _seed = randint(0, int(time()))
        print(_seed)
        seed(_seed)

        last_rolls.update({mes.from_user.id: context.args})

        rolls_temp = [str(randint(1, int(d_type)+1)) for _ in range(0, int(k))]
        rolls.append(f"<b>Rolling {k}d{d_type}:</b> <span class=\"tg-spoiler\">{' '.join(rolls_temp)}</span>\n")
        total += sum([int(x) for x in rolls_temp])

    rolls.append(f"\n<b>Total:</b> <span class=\"tg-spoiler\">{total}</span>")

    await mes.reply_text(text="".join(rolls),
                         parse_mode="HTML")


async def reroll(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mes = update.message

    if mes.from_user.id not in last_rolls:
        await mes.reply_text(text="<b>You didn't roll yet :c</b>",
                             parse_mode="HTML")
        return

    context.args = last_rolls.get(mes.from_user.id)

    await roll(update, context)
