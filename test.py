# import requests
# from bs4 import BeautifulSoup
#
# req = requests.get('http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')
# html = req.text
# soup = BeautifulSoup(html, 'html.parser')
# posts = soup.find("tr", {"class": "list1"})
# link = 'http://www.ppomppu.co.kr/zboard/'+posts.find("td", { "valign" : "middle"}).find("a").attrs['href']
#
# text_req = requests.get(link)
# text_html = text_req.text
# text_soup = BeautifulSoup(text_html, 'html.parser')
# text_link = text_soup.find("div", {"class" : "wordfix"}).find("a").text
#
# print(text_link)

happy = '2911-3344-6199-5932_20200701, 2911-3344-9066-4281_20200701, 2911-3344-9191-5379_20200701, 2911-3750-3385-0619_20200701, 2911-3750-3865-2688_20200701, 2911-3750-8890-3848_20200701, 2911-3750-8367-9224_20200701, 2911-3751-8363-0432_20200701, 2911-3751-3363-4363_20200701, 2911-3751-3828-6283_20200701'
bookand = '8081709159550375_8503, 8016709659530376_8884, 8010709059500377_8227, 8017709759590378_8686, 8046709659540379_8001, 8019709959570380_8240, 8017709759500381_8029, 8040709059580382_8466, 8042709259550383_8505, 8042709259560384_8020, 8064709459530385_8185, 8007709759540386_8608, 8045709559560387_8623, 8088709859530388_8082, 8085709559500389_8625, 8062709259530390_8682, 8036709659560391_8025, 8095709559580392_8260, 8008709859570393_8149, 8062709259540394_8606'

# happy_ = happy.split(', ')
# for i in range(10):
#     print(i+1, happy_[i])

bookand_ = bookand.split(', ')
for i in range(20):
    bookand__ = bookand_[i]
    print(i+1, bookand__[:4], bookand__[4:8], bookand__[8:12], bookand__[12:16], bookand__[17:])
    if (i+1)%5 == 0:
        print('\n')