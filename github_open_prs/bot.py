# first install telegram package: pip3 install python-telegram-bot
import telegram
import os
from github_prs import prs_sdk, prs_jsng, prs_charts

#token that can be generated talking with @BotFather on telegram
my_token = 'bot_token'

def send(msg, chat_id, token=my_token):
    """
    Send a mensage to a telegram user specified on chatId
    chat_id must be a number!
    """
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=msg)

if __name__ == "__main__":
    msgs = [prs_jsng, prs_sdk, prs_charts]
    github_prs_token = os.environ.get("PRs_TOKEN")
    chat_id = os.environ.get("CHAT_ID_OPEN_PRs")

    for m in msgs:
        separator = '\n'
        if len(m) > 1:
            ms = separator.join(m)
            send(msg=ms, chat_id=chat_id, token=github_prs_token)
