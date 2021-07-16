import requests
import os
import json
from task_1 import (scrape_top_list,readingfile,wrting_file)



def analyse_language_and_directors():
    movie_details=readingfile("movie_details.json")
    dic1={}
    for i in movie_details:
        for j in i["director"]:
            dic1[j]={}
    for director in dic1:
        for dic_movie in movie_details:
            if director in dic_movie["director"]:
                for eachlang in dic_movie["languge"]:
                    langCount=0
                    dic1[director][eachlang]=langCount
                    for each_dict in movie_details:
                        if (eachlang in each_dict["languge"]) and (director in each_dict["director"]):
                            dic1[director][eachlang]+=1
    file=wrting_file("count_lang_directors.json",dic1)
analyse_language_and_directors()