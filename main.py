from multiprocessing import Process
from telegram_p import telegram_p
from crawling_p import crawling_p

if __name__ == '__main__':
    main_p = Process(target=telegram_p, args=())
    sub_p = Process(target=crawling_p, args=())
    main_p.start()
    sub_p.start()