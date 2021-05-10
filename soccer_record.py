from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("https://sports.news.naver.com/wfootball/record/index.nhn?category=epl&tab=player")

soup=BeautifulSoup(html, "lxml")
wfootballPRB = soup.find_all('div', {"id":"wfootballPlayerRecordBody"})

wfootballPRB_tbody=wfootballPRB[0].find_all("tbody")
wfootballPRB_tbody_row=wfootballPRB_tbody[0].find_all("tr")
