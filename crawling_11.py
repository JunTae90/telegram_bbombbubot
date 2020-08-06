import requests
from bs4 import BeautifulSoup
import telegram
import os
import time

my_token = '1254468459:AAHMs1f2LqZBQQUJW7f_i3bkmNdFF2zuz1c'
bot = telegram.Bot(my_token)
data_dir = 'data'
def update_user():
    for root, dirs, files in os.walk(data_dir):
        return files

def update_post():
    soldout_latest = False
    while True:
        user_list = update_user()
        try:
            link = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=2778024489&xfrom=&xzone='
            req_headers = {'User-Agent':('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'),}
            req = requests.get(link, headers=req_headers)
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
            text_em_lg = soup.find("p", {"class", "text_em_lg"}).text
            print(text_em_lg)
            if "품절" in text_em_lg:
                soldout_current = True
            else:
                soldout_current = False
        
            if(soldout_latest != soldout_current):
                soldout_latest = soldout_current
                if(soldout_current):
                    message = '11번가 해피머니 5만원권 매진 알림'
                else:
                    message = '11번가 해피머니 5만원권 재입고 알림'
                message += '\n' + link
                for user in user_list:
                    try:
                        bot.sendMessage(user, message)
                    except telegram.error.Unauthorized:
                        os.remove(os.path.join(data_dir, user))
                        continue
        except:
            continue
        time.sleep(0.5)
        


def crawling_11():
    update_post()

if __name__ == "__main__":
    crawling_11()