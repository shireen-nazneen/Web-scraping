
from bs4 import BeautifulSoup
import requests
import json
from requests import models

# function for reading file
def readingfile(filename):
    with open(filename,"r") as f:
        x=json.load(f)
        return(x)
    


# function for  making file

def wrting_file(filename,var):
    with open(filename,"w") as f:
        json.dump(var,f,indent=4)


# function for making for maive name 
def convert_int(var):
    i=0
    k=" "
    while i<len(var):
        if i==0 or i==5:
            i+=1
            continue
        k+=(var[i])
        i+=1
    return(k)
print(convert_int("(1990)"))
# function for making list  years
def making_list(dict):
    list1=[]
    for i in dict:
        k=i["relesing_year"]
        list1.append(k)
    return list1

# task one scrap top list movie
imdb_page=requests.get('https://www.imdb.com/india/top-rated-indian-movies/').text
imdb_page_soup=BeautifulSoup(imdb_page,"html.parser")
searching_tbody=imdb_page_soup.find("tbody",class_="lister-list")
trfind=searching_tbody.find_all("tr")
def scrape_top_list():
    trfind=searching_tbody.find_all("tr")
    list_movies=[]
    movie_position=1
    for i in trfind:
        find_td_movie=i.find("td",class_="titleColumn").a.get_text()
        movie_rating=i.find("td",class_="ratingColumn imdbRating").get_text()
        movie_link=i.find("td",class_="titleColumn").a["href"]
        find_movie_year=i.find("span",class_="secondaryInfo").get_text()
        year=convert_int(find_movie_year)
        year=int(year)
        dic1={"movie":find_td_movie,"rating":float(movie_rating),"url":"https://www.imdb.com"+movie_link,"position":movie_position,"relesing_year":year}
        list_movies.append(dic1)
        movie_position+=1
        # print(list_movies)
    filewriting=wrting_file("top_list_task_1.json",list_movies)
    return(list_movies)
# print(scrape_top_list())
movie=scrape_top_list()