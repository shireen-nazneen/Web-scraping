from bs4 import BeautifulSoup
from bs4.element import ProcessingInstruction
import requests
import json
from requests import models
from task_1 import (making_list, wrting_file ,readingfile)
from task_1 import scrape_top_list
from task_4 import scrape_movie_details


movie=scrape_top_list()
def get_movie_list_details():
    count=1
    list_movie_details=[]
    for j in movie:
        link=(j["url"])
        making_list_details=scrape_movie_details(link,j["movie"])
        print(making_list_details)
        list_movie_details.append(making_list_details)
        print(count)
        count+=1
    file=wrting_file("movie_details.json",list_movie_details)
    return list_movie_details
get_movie_list_details()
