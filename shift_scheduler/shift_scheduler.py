
from datetime import datetime
import telegram
import os


# def when_is_my_turn_testing(name):
#     delta = len(team) - team.index(name)
#     message = "your turn is in %i weeks" % delta



# def when_is_my_turn_chats(name):
#     delta = len(team) - team.index(name)
#     message = "your turn is in %i weeks" % delta




if __name__ == '__main__':
    def update_pointer(pointer_name):
        length = len(team)
        current_pointer = pointers[pointer_name]
        current_pointer += 1
        if current_pointer == length:
            current_pointer = 0
            
        pointers[pointer_name] = current_pointer
        with open('pointers', 'w') as f:
            f.write(pointers)
    
    
    def schedule_suite_tests(bot):
        turn  = team.get(pointers['test'], '@rthursday')
        message = "%s, today, it's your turn to run the testlodge scenarios" % turn
        bot.sendMessage(chat_id=chat_id, text=message)
        update_pointer('test')


    def schedule_chat_babysitting(bot):
        turn  = team.get(pointers['chat'], '@rthursday')
        message = "%s, for this week, it's your turn to babysit the chats" % turn
        bot.sendMessage(chat_id=chat_id, text=message)
        update_pointer('chat')
        
    
    token =  os.environ.get("BOT_SHIFT_SCHEDULER")
    chat_id = os.environ.get("CHAT_ID_SCHEDULER")


    try:
        with open('pointers', 'r') as f:
            pointers = f.read()
        pointers = eval(pointers)
    except Exception as e:
        pointers = {'chat': 0, 'test': 0}


    team = ['@sameh_farouk', '@waleedhammam', '@ranatrk',
            '@melborolossy', '@abomdev', '@ahmedhanafy725', 
            '@RafyBenjamin', '@mr_conflict', '@dmahmou'] # @oElawady
    bot = telegram.Bot(token=token)

    
    schedule_suite_tests()

    if datetime.today().isoweekday() == 7: # Sunday
        schedule_chat_babysitting()

    


    
