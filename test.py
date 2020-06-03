import requests
from bs4 import BeautifulSoup

req = requests.get('http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
posts = soup.find("tr", {"class": "list1"})
link = 'http://www.ppomppu.co.kr/zboard/'+posts.find("td", { "valign" : "middle"}).find("a").attrs['href']

text_req = requests.get(link)
text_html = text_req.text
text_soup = BeautifulSoup(text_html, 'html.parser')
text_link = text_soup.find("div", {"class" : "wordfix"}).find("a").text

print(text_link)
