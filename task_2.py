from os import remove
from re import findall
from sys import modules
from bs4 import BeautifulSoup
import requests
import json
from requests import models
from task_1 import wrting_file
from task_1 import  scrape_top_list
 


# task 2
movies=scrape_top_list()
def group_by_year(movies):
    unique_years=[]
    for i in movies:
        year_u=i["relesing_year"]
        if year_u not in unique_years:
            unique_years.append(year_u)
    movies_dict={}
    for  j in unique_years:
        movies_dict[j]=[]
    for k in movies:
        year=k["relesing_year"]
        if year in movies_dict:
            movies_dict[year].append(k)
    filewriting=wrting_file("groub_by_year.json",movies_dict)
    return unique_years
# group_by_year(movies)