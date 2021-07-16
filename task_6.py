from requests.api import get
# from task_4 import scrape_movie_details
# from task_5 import get_movie_list_details
import json
import requests
from task_1 import (readingfile, wrting_file)
def analyse_movies_language():
    data=readingfile("movie_details.json")
    dic1={}
    list_lan=[]
    for i in data:
        for j in i["languge"]:
            if j not in dic1.keys():
                c=0
                for z in data:
                    for k in z["languge"]:
                        if j==k:
                            c+=1
                dic1[j]=c
    writing_file=wrting_file("countlanguge.json",dic1)
analyse_movies_language()
    
