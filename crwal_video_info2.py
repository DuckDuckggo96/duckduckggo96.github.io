import requests
from bs4 import BeautifulSoup
import time
import urllib.request #
from selenium.webdriver import Chrome
import re
import  pandas as pd


from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
import datetime as dt

#click 할떄는 xpath..
#특정 텍스트나 url 찾을때는 find,findall
def func_video_crall(url):
    delay = 3
    browser = Chrome()
    browser.implicitly_wait(delay)
    start_url = url
    browser.get(start_url)
    browser.maximize_window()
    num_of_pagedowns=3
    while num_of_pagedowns:
        browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        num_of_pagedowns-=1
    soup=BeautifulSoup(browser.page_source,'html.parser')
    info1 = soup.find('div',{'id':'info-contents'})
    comm=soup.find('ytd-comments',{'id':'comments'})
    comment1 = soup.find('yt-formatted-string', {'class': 'count-text style-scope ytd-comments-header-renderer'}).text
    comment2 = comm.findAll('yt-formatted-string', {'class': 'style-scope ytd-comment-renderer'})
    title = info1.find('h1',{'class':'title style-scope ytd-video-primary-info-renderer'}).text #영상제목
    view =info1.find('yt-view-count-renderer',{'class':'style-scope ytd-video-primary-info-renderer'}).find_all('span')[0].text #영상 조회수
    like = info1.find('div',{'id':'top-level-buttons'}).find_all('yt-formatted-string')[0].text #좋아요수
    unlike = info1.find('div',{'id':'top-level-buttons'}).find_all('yt-formatted-string')[1].text #싫어요수
    date = soup.find('span',{'class':'date style-scope ytd-video-secondary-info-renderer'}).text#영상업로드날
    youtube_info={"title":title, "view":view,"like":like,"unlike":unlike,"date":date}
    asd=soup.find_all('div',{'id':'header-author'},{'class':'style-scope ytd-comment-renderer'})
    print("youtube_info")
    print(youtube_info)
    #print(comment1)
    #print(comm)
    #print(title)
    #print(view)
    #print(like)
    #print(unlike)
    #print(date)
    cmtlist=[]
    cmt_ll=[]
    ex_list=[]
    for items in soup:
        div=items.find_all('yt-formatted-string',attrs={'id':'content-text'})  #comment
        div2=items.find_all('span',attrs={'class':'style-scope ytd-comment-renderer'})
        for list2 in div2:
            if (list2.string != None) and (list2.string != 'VIEW'):
                ccc=(list2.string.replace('\n',"")).strip()
                if(ccc != '•') and (ccc != ''):
                    cmt_ll.append([ccc])
        for lists in div:
            if lists != None:
                try:
                    cmt=lists.string
                    cmtlist.append([cmt])
                except TypeError as e:
                    pass
                else:
                    pass

    casd={"comment" : cmtlist , "comment_id" : cmt_ll}
    #
    # frame=pd.DataFrame(casd)
    # print(frame)
    # frame.to_csv("frame.csv",mode="w",encoding="utf-8-sig")

    return cmtlist


