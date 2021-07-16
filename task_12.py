# from os import link
from sys import implementation
import requests
import json
from requests import models
from task_1 import (wrting_file ,readingfile,scrape_top_list)
import random
import time
from bs4 import BeautifulSoup
import requests
import json
import os




# movie_name="Dangal"
# link="https://www.imdb.com/title/tt5074352/"
# def cast(link):
#     list_actor=[]
#     url_page=(requests.get(link)).text
#     url_page_soup=BeautifulSoup(url_page,"html.parser") 
#     find_div_page=url_page_soup.find("div",class_="ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--wraps-at-above-l title-cast__grid")
#     find_a_div=find_div_page.select("a[data-testid='title-cast-item__actor']")
#     for actor in find_a_div:
#         print(actor.text)
#         link_actor=actor["href"]
#         link=link_actor[6:15]
#         dict={"actor_name":actor.text,"imdb_id":link}
#         print(dict)
#         list_actor.append(dict)
#     wrting_file_=wrting_file("actors.json",list_actor)
#     return list_actor
# # print(cast(link))


movie_name="Dangal"
link="https://www.imdb.com/title/tt5074352/"
file="/home/shireen/Desktop/webscarping/all_file/"+"tt5074352"+".text"
def cast(link,file):
    list_actor=[]
    print(os.path.exists(file))
    if (os.path.exists(file)):
        f=open(file,"r")
    url_page_soup=BeautifulSoup(f,"html.parser") 
    find_div_page=url_page_soup.find("div",class_="ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--wraps-at-above-l title-cast__grid")
    find_a_div=find_div_page.select("a[data-testid='title-cast-item__actor']")
    for actor in find_a_div:
        print(actor.text)
        link_actor=actor["href"]
        link=link_actor[6:15]
        dict={"actor_name":actor.text,"imdb_id":link}
        print(dict)
        list_actor.append(dict)
    wrting_file_=wrting_file("actors.json",list_actor)
    return list_actor
print(cast(link,file))






