# import json
# from typing import cast
# import requests
from typing import cast
from task_1 import (wrting_file,readingfile)
from task_1 import *


#analayes cast 

movie_details=readingfile("movie_details_with_cast.json")
list_cast={}
for movie in movie_details:
    cast_list=movie["cast"]
    for i in range(5):
        imdbid=cast_list[i]["imdb_id"]
        name=cast_list[i]["actor_name"]
        list_cast[imdbid]={"name":name,"frequent_co_actors":[]}
for cast_actors in list_cast:
    print(cast_actors)
    for movie_dic in movie_details:
        cast_l=movie_dic["cast"]
        flag=False
        for c in cast_l:
            if c["imdb_id"]==cast_actors:
                flag=True
                break
               # it is incomplete
                
                
        #i will complate it soon 
