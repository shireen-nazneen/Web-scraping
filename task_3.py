from os import remove
from re import findall
from sys import modules
from bs4 import BeautifulSoup
import requests
import json
from requests import models
from task_1 import wrting_file , scrape_top_list, readingfile
from task_2 import group_by_year

def making_list(dict):
    list1=[]
    for i in dict:
        k=i["relesing_year"]
        list1.append(k)
    return list1
movies=scrape_top_list()
def group_by_decade(movies):
    list_year=making_list(movies)
    for i in movies:
        empty_list_dec=[]
        for j in list_year:
            m=j%10
            dec=j-m
            if dec not in empty_list_dec:
                empty_list_dec.append(dec)
        empty_list_dec.sort()
        movies_d={}
        for l in empty_list_dec:
            movies_d[l]=[]
        for m in movies_d:
            dic10=m+9
            for k in movies:
                year_k=k["relesing_year"]
                if  year_k<=dic10  and year_k>=m:
                    movies_d[m].append(k)
        filewriting=wrting_file("group_by_decade.json",movies_d)
group_by_decade(movies)