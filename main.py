from multiprocessing import Process
from telegram_p import telegram_p
from crawling_p import crawling_p
from crawling_11 import crawling_11

if __name__ == '__main__':
    main_p = Process(target=telegram_p, args=())
    sub_p = Process(target=crawling_p, args=())
    eleven_p = Process(target=crawling_11, args=())
    main_p.start()
    sub_p.start()
    eleven_p.start()
    main_p.join()
    sub_p.join()
    eleven_p.join()