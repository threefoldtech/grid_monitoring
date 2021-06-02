# first install telegram package: pip3 install python-telegram-bot
import telegram
import os
import issues_status 

#token that can be generated talking with @BotFather on telegram
my_token = 'bot_token'

def send(msg, chat_id, token=my_token):
    """
    Send a mensage to a telegram user specified on chatId
    chat_id must be a number!
    """
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=msg, parse_mode="Markdown", disable_web_page_preview=True)

if __name__ == "__main__":
    msgs = issues_status.get_status()
    bot_issues_status_token =  os.environ.get("BOT_ISSUES_STATUS")
    chat_id = os.environ.get("CHAT_ID_ISSUES_STATUS")

    for m in msgs:
        send(msg=m, chat_id=chat_id, token=bot_issues_status_token)
