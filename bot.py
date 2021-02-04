# first install telegram package: pip3 install python-telegram-bot
# cronjob: cd ~/js-sdk/ && git checkout development_vdc && poetry shell & python3 ~/grid_monitoring/bot.py
import grid_monitoring as gm
import telegram
import os

#token that can be generated talking with @BotFather on telegram
my_token = 'bot_token'

def send(msg, chat_id, token=my_token):
    """
    Send a mensage to a telegram user specified on chatId
    chat_id must be a number!
    """
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=msg)

class Test:
    pass

if __name__ == "__main__":
    my_token = os.environ.get("TOKEN")
    chat_id = os.environ.get("CHAT_ID")
    self = Test()
    gm_result = gm.check_grid(self)
    for errors in gm_result:
        if errors:
            separator = '\n'
            m = separator.join(errors)
            
            send(msg=m, chat_id=chat_id, token=my_token)
