import logging
import sys

from telegram import Update
from telegram.ext import Application, CommandHandler
from roll import roll, reroll, help

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

TOKEN = ""

if len(sys.argv) >= 3 and sys.argv[1].lower() == "--token":
    TOKEN = sys.argv[2]
else:
    raise RuntimeError("Missing --token argument (please README, I beg you)")


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler(["roll", "r"], roll))
    application.add_handler(CommandHandler(["reroll", "rr"], reroll))
    application.add_handler(CommandHandler("help", help))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
