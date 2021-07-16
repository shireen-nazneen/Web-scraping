import json
# from task_6 import analyse_movies_language
import requests
from task_1 import (readingfile, wrting_file)

data=readingfile("movie_details.json")
def analyse_movies_directors():
    dic1={}
    list_lan=[]
    for i in data:
        for j in i["director"]:
            if j not in dic1.keys():
                c=0
                for z in data:
                    for k in z["director"]:
                        if j==k:
                            c+=1
                dic1[j]=c
    writingfile=wrting_file("directors.json",dic1)
analyse_movies_directors()