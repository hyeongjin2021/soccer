from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("https://sports.news.naver.com/wfootball/record/index.nhn?category=epl&tab=player")

soup=BeautifulSoup(html, "lxml")
wfootballPRB = soup.find_all('div', {"id":"wfootballPlayerRecordBody"})

wfootballPRB_tbody=wfootballPRB[0].find_all("tbody")
wfootballPRB_tbody_row=wfootballPRB_tbody[0].find_all("tr")

print('================================================================')
a=input('1,2,3 중 하나 입력:')
footballPRB1=[] #리스트의 리스트
count=0
for tr in wfootballPRB_tbody_row:
    PRB=[]
    td=tr.find_all("td")
    for record in td:
        print(record.get_text().strip("\n\n"),end=",")
        PRB.append(record.get_text().strip('\n\n\n'))
    print("")
    count=count+1
    if count == 10:
        break
    footballPRB1.append(PRB)

name=[]
score=[]
assist=[]


print('리스트:',footballPRB1)

print(footballPRB1)
 #그래프에서 이용할 리스트
for PRB in footballPRB1:
    name1,team=PRB[1].split('\n')

    name.append(name1) #선수명
    score.append(int(PRB[2]))   #득점
    assist.append(int(PRB[3]))   #도움
score_score=[]
assist_assist=[]
for i in range(20):
    score_score.append(score[i])
    assist_assist.append(assist[i])

print('선수명 팀:',name)
print('득점:',score_score)
print('도움:',assist_assist)


import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Malgun Gothic')

if a=='2':
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    plt.yticks(x, name)
    plt.barh(x, score_score, label='득점', color='b')
    plt.barh(x, assist_assist, label='도움', color='g')
    plt.legend()
    plt.show()
