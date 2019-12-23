import requests
from bs4 import BeautifulSoup
import time
import urllib.request #
from selenium.webdriver import Chrome
import re
import  pandas as pd
# from  crwal_video_info import func_video_crall
from konlpy.tag import  Twitter
from  crwal_video_info2 import  func_video_crall
from  mining import get_noun
from mining import mining

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
import datetime as dt

#click 할떄는 xpath..
#특정 텍스트나 url 찾을때는 find,findall
delay=3
browser=Chrome()
browser.implicitly_wait(delay)
num_of_pagedown = 7
start_url="https://www.youtube.com/channel/UCdUcjkyZtf-1WJyPPiETF1g"
browser.get(start_url)
browser.maximize_window()
browser.find_element_by_xpath('//*[@class="scrollable style-scope paper-tabs"]/paper-tab[2]').click()
browser.find_element_by_xpath('//*[@id="sort-menu"]').click()
while(True):
    try:
        browser.find_element_by_xpath(
            '//*[@id="menu"]/a[1]/paper-item/paper-item-body/div[text()="인기 동영상"]').click()  # 문제있네.. 클릭이 됐다 왠댔다..
        break
    except Exception as e:
        pass
ex_list=[]
html=BeautifulSoup(browser.page_source,'html.parser')
video_ls=html.find_all('ytd-grid-video-renderer',attrs={'class':'style-scope ytd-grid-renderer'})
video_listUrl=[]
for i in range(len(video_ls)):
    video_listUrl.append("https://www.youtube.com"+video_ls[i].find('a',attrs={'id':'thumbnail'})['href'])
    # print(video_listUrl[i])

for i in  range(1):
    # ex_list.append(func_video_crall(video_listUrl[i]))
    ex_list.append(func_video_crall(video_listUrl[i]))
# -----------------------------------
comment_result=mining(ex_list)

comment_result['token'] = comment_result['comment'].apply(lambda x :get_noun(x))
# konlpy lambda 공부...
for i in comment_result:
    print(i)