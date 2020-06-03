import pickle
import os
import requests
from bs4 import BeautifulSoup
import telegram
import threading
import time

my_token = '1254468459:AAHMs1f2LqZBQQUJW7f_i3bkmNdFF2zuz1c'
bot = telegram.Bot(my_token)
data_dir = 'data'
my_dict = {}
def update_keyword():
    my_dict.clear()
    for root, dirs, files in os.walk('data'):
        for fname in files:
            full_fname = os.path.join(root, fname)
            try:
                with open(full_fname, 'rb') as fr:
                    data = pickle.load(fr)
                    for keyword in data:
                        try:
                            my_dict[keyword].append(fname)
                            my_dict[keyword] = list(set(my_dict[keyword]))
                        except:
                            my_dict[keyword] = [fname]
            except:
                continue
        print(my_dict)

def update_post():
    latest_num = 0
    while True:
        update_keyword()
        keyword_list = list(my_dict.keys())
        req = requests.get('http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        posts = soup.find("tr", {"class" : "list1"})
        current_num = posts.find("td", {"class" : "eng list_vspace"}).text
        title = posts.find("font", {"class" : "list_title"}).text
        if latest_num != current_num:
            latest_num = current_num
            for keyword in keyword_list:
                if keyword in title:
                    link = 'http://www.ppomppu.co.kr/zboard/'+posts.find("td", { "valign" : "middle"}).find("a").attrs['href']
                    message = '<뽐뿌 키워드 탐색>' + '\n' + title + '\n' + link
                    user_list = my_dict[keyword]
                    for user in user_list:
                        try:
                            bot.sendMessage(user, message)
                        except telegram.error.Unauthorized:
                            os.remove(os.path.join(data_dir, user))
                            continue

        time.sleep(0.5)

def crawling_p():
    update_post()

if __name__ == '__main__':
    crawling_p()


