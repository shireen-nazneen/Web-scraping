import os
from typing import Text 
# import json
from task_1  import (scrape_top_list,readingfile,wrting_file)
# from requests import models
from bs4 import BeautifulSoup
import requests 
# import time
# import random
from os import write




def mange_movie_name(name):
    s=""
    for i in name:
        if "(" not in i:
            s+=i
        else:
            break
    return s
movie_details=scrape_top_list()
def creat_text_files():
    for i in range(len(movie_details)):
        url=movie_details[i]["url"]
        url_page=requests.get(url)
        # url_page_soup=BeautifulSoup(url_page.text,"html.parser")
        link=url[27:]
        id=""
        for i in link:
            if "/"!=i:
                id+=i
            else:
                break
        p="/home/shireen/Desktop/webscarping/all_file/"+id+".text"
        if  not(os.path.exists(p)):
            f=open(p,"w")
            f1=f.write(url_page.text) 
        else:
            print("allrady _exsist")
creat_text_files()  


