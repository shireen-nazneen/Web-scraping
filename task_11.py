import requests
import os
import json
from task_1 import (scrape_top_list,readingfile,wrting_file)



def analyse_language_and_gener():
    movie_details=readingfile("movie_details.json")
    dic1={}
    list_lan=[]
    for i in movie_details:
        for j in i["genre"]:
            if j not in dic1.keys():
                c=0
                for z in movie_details:
                    for k in z["genre"]:
                        if j==k:
                            c+=1
                dic1[j]=c   
    file=wrting_file("count_genres.json",dic1)
analyse_language_and_gener()