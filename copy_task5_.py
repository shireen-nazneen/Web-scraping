
# from bs4 import BeautifulSoup
# import requests
# import json
# from requests import models
# from task_1 import (wrting_file ,readingfile)

# def wrting_file(filename,var):
#     with open(filename,"w")as f:
#         json.dump(var,f,indent=4)
# def mange_movie_name(name):
#     s=""
#     for i in name:
#         if "(" not in i:
#             s+=i
#         else:
#             break
#     return s

# def scrape_movie_details():
#     list_movie_details=[]
#     count1=1
#     url_movie=readingfile("top_list_task_1.json")
#     for j in url_movie:
#         url_page=requests.get(j["url"]).text
#         url_page_soup=BeautifulSoup(url_page,"html.parser")
#         print(url_page_soup)
#         # find_td_movie=url_page_soup.find("div",class_="title_wrapper").h1.get_text()
#         movie=j["movie"]
#         find_subtex=url_page_soup.find("div",class_="subtext")
#         runtime_text=find_subtex.find("time").get_text().strip()
#         runtime=int(runtime_text[0])*60
#         if "min" in runtime_text:
#             min=runtime_text[3:]
#             s=" "
#             for i in min:
#                 if i=="m" or i=="i" or i=="n":
#                     continue
#                 else:
#                     s+=i
#             runtime=runtime+int(s)
#         else:
#             runtime=runtime
#         summary=url_page_soup.find("div",class_="plot_summary")
#         movie_bio=summary.find("div",class_="summary_text").get_text().strip()
#         director_div=summary.find("div",class_="credit_summary_item")
#         find_a_dire=director_div.find_all("a")
#         director_list=[d.get_text() for d in find_a_dire]
#         mainDiv=url_page_soup.find("div",{"id":"titleStoryLine"})
#         find_see_more=mainDiv.find_all("div",class_="see-more inline canwrap")
#         if len(find_see_more)>1:
#             find_a_genre=find_see_more[1].find_all("a")
#             genre_list=[d.get_text() for d in find_a_genre]
#         else:
#             pass
#         details=url_page_soup.find("div",{"id":"titleDetails"})
#         find_div_b=details.find_all("div",class_="txt-block")
#         if find_div_b[0].find("h4").text=="Country:":
#             country=find_div_b[0].find("a").text
#             languge=find_div_b[1].find("a").text
#         else:
#             country=find_div_b[1].find("a").text
#             languge=find_div_b[2].find("a").text
#         find_poster_img=url_page_soup.find("div",class_="poster")
#         poster=find_poster_img.find("a")
#         img=poster.find("img")["src"]
#         dic2={"name":movie,"bio": movie_bio , "director":director_list,"languge": languge,"country":country,"genre":genre_list,"runtime": runtime,"posterurl":img}
#         list_movie_details.append(dic2)

#         count1+=1
#         break
#     writetingfile=wrting_file("movie_details.json",list_movie_details) 
# scrape_movie_details()



