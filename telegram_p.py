from telegram_bot import MyBot
import os
import pickle

my_token = '1254468459:AAHMs1f2LqZBQQUJW7f_i3bkmNdFF2zuz1c'
data_dir = 'data'

def keyword(bot, update):
    chat_id = update.message.chat.id
    filename = str(chat_id)
    with open(os.path.join(data_dir, filename), 'rb') as fr:
        keyword_list = pickle.load(fr)
    message = '현재 키워드 목록은 아래와 같습니다.'
    message += '\n============================'
    for i in keyword_list:
        message += '\n' + i
    bot.sendMessage(chat_id, message)

def delete(bot, update):
    chat_id = update.message.chat.id
    filename = str(chat_id)
    order = update.message.text.split(' ')
    if len(order) == 2:
        keyword = order[1]
        if not os.path.exists(os.path.join(data_dir, filename)):
            with open(os.path.join(data_dir, filename), 'wb') as fw:
                pickle.dump([], fw)
        with open(os.path.join(data_dir, filename), 'rb') as fr:
            keyword_list = pickle.load(fr)
        if keyword in keyword_list:
            keyword_list.remove(keyword)
            with open(os.path.join(data_dir, filename), 'wb') as fw:
                pickle.dump(keyword_list, fw)
            message = '키워드가 삭제되었습니다.\n현재 키워드 목록은 아래와 같습니다.'
            message += '\n============================'
            for i in keyword_list:
                message += '\n' + i
            bot.sendMessage(chat_id, message)
        else:
            message = '존재하지 않는 키워드입니다.\n현재 키워드 목록은 아래와 같습니다.'
            message += '\n============================'
            for i in keyword_list:
                message += '\n' + i
            bot.sendMessage(chat_id, message)
    else:
        message = '형식을 지켜주세요.\n/delete "키워드"'
        bot.sendMessage(chat_id, message)

def add(bot, update):
    chat_id = update.message.chat.id
    filename = str(chat_id)
    order = update.message.text.split(' ')
    if len(order) == 2:
        keyword = order[1]
        if not os.path.exists(os.path.join(data_dir, filename)):
            with open(os.path.join(data_dir, filename), 'wb') as fw:
                pickle.dump([], fw)
        with open(os.path.join(data_dir, filename), 'rb') as fr:
            keyword_list = pickle.load(fr)
        keyword_list.append(keyword)
        keyword_list = list(set(keyword_list))
        with open(os.path.join(data_dir, filename), 'wb') as fw:
            pickle.dump(keyword_list, fw)

        message = '키워드가 추가되었습니다.\n현재 키워드 목록은 아래와 같습니다.'
        message += '\n============================'
        for i in keyword_list:
            message += '\n' + i
        bot.sendMessage(chat_id, message)
    else:
        message = '형식을 지켜주세요.\n/add "키워드"'
        bot.sendMessage(chat_id, message)

def start(bot, update):
    chat_id = update.message.chat.id
    filename = str(chat_id)
    if not os.path.exists(os.path.join(data_dir, filename)):
        with open(os.path.join(data_dir, filename), 'wb') as fw:
            pickle.dump([], fw)
        bot.sendMessage(chat_id, '유저가 등록되었습니다.\n이용방법은 아래를 참조하세요.\n/start : 유저등록\n/add “keyword” : “keyword” 등록\n/delete “keyword” : “keyword” 삭제\n/keyword : 현재 등록된 키워드 목록 출력')
    else:
        bot.sendMessage(chat_id, '기 등록된 유저입니다.\n이용방법은 아래를 참조하세요.\n/start : 유저등록\n/add “keyword” : “keyword” 등록\n/delete “keyword” : “keyword” 삭제\n/keyword : 현재 등록된 키워드 목록 출력')

def telegram_p():
    bot = MyBot(my_token)
    bot.add_handler('start', start)
    bot.add_handler('add', add)
    bot.add_handler('delete', delete)
    bot.add_handler('keyword', keyword)
    bot.start()


