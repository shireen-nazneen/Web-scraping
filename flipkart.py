import collections
from selenium import webdriver
import requests
import json
from bs4 import BeautifulSoup
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys


# def scrapping_details():
#     browser=webdriver.Chrome(executable_path="/home/shireen/Downloads/chromedriver_linux64/chromedriver")
#     browser.get("https:flipkart.com")
#     PhoneNumber=browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input")
#     PhoneNumber.send_keys("7411897682")
#     password=browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input")
#     password.send_keys("9902232446")
#     enter=browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button").click()
#     enterinput=browser.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
#     enterinput.send_keys("biba")
#     findoutput=browser.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
#     findoutput.send_keys(Keys.ENTER)
#     i=1
#     list_ofdress=[]
#     while True:
#         page=requests.get("https://www.flipkart.com/search?q=biba&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i))
#         find_page=find("div",class_="ge-49M")
#         clothlink=requests.get("https://www.flipkart.com/biba-women-printed-straight-kurta/p/itm476d2ee969d23?pid=KRTF7DWCUDAQZPDY&lid=LSTKRTF7DWCUDAQZPDYRKZEMT&marketplace=FLIPKART&q=biba&store=clo&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=4bd005af-d710-489f-b636-eb76123f341e.KRTF7DWCUDAQZPDY.SEARCH&ppt=sp&ppn=sp&ssid=eeciuchfcw0000001622700638950&qH=931691969b142b3a").text
#         soup=BeautifulSoup(page,"html.parser")
#         brand=soup.find("h1",class_="yhB1nd").text
#         actual_price=soup.find(class_="_30jeq3 _16Jk6d").text
#         price=soup.find(class_="_3I9_wc _2p6lqe").text
#         find_rateing=soup.find(id="productRating_LSTKRTF7DWCUDAQZPDYRKZEMT_KRTF7DWCUDAQZPDY_").text
#         find_off=soup.find("div",class_="_3Ay6Sb _31Dcoz pZkvcx").text
#         find_retun_policy=soup.find("div",class_="_2MJMLX").text
#         dic_informetion={"brand":brand,"amount":actual_price,"selling_price":price,"rating":find_rateing,"offer":find_off,"return":find_retun_policy}
#         print(dic_informetion)
#         list_ofdress.append(dic_informetion)
#     i+=1


def scrapping_details():
    browser=webdriver.Chrome(executable_path="/home/shireen/Downloads/chromedriver_linux64/chromedriver")
    browser.get("https:flipkart.com")
    print(browser.page_source)
    PhoneNumber=browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input")
    PhoneNumber.send_keys("7411897682")
    password=browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input")
    password.send_keys("9902232446")
    enter=browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button").click()
    enterinput=browser.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
    enterinput.send_keys("biba")
    findoutput=browser.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
    findoutput.send_keys(Keys.ENTER)
    i=1
    list_ofdress=[]
    while True:
        page=requests.get("https://www.flipkart.com/search?q=biba&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i))
        print(browser.page_source)
        clothlink=requests.get("https://www.flipkart.com/biba-women-printed-straight-kurta/p/itm476d2ee969d23?pid=KRTF7DWCUDAQZPDY&lid=LSTKRTF7DWCUDAQZPDYRKZEMT&marketplace=FLIPKART&q=biba&store=clo&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=4bd005af-d710-489f-b636-eb76123f341e.KRTF7DWCUDAQZPDY.SEARCH&ppt=sp&ppn=sp&ssid=eeciuchfcw0000001622700638950&qH=931691969b142b3a").text
        soup=BeautifulSoup(page,"html.parser")
        brand=soup.find("h1",class_="yhB1nd").text
        actual_price=soup.find(class_="_30jeq3 _16Jk6d").text
        price=soup.find(class_="_3I9_wc _2p6lqe").text
        find_rateing=soup.find(id="productRating_LSTKRTF7DWCUDAQZPDYRKZEMT_KRTF7DWCUDAQZPDY_").text
        find_off=soup.find("div",class_="_3Ay6Sb _31Dcoz pZkvcx").text
        find_retun_policy=soup.find("div",class_="_2MJMLX").text
        dic_informetion={"brand":brand,"amount":actual_price,"selling_price":price,"rating":find_rateing,"offer":find_off,"return":find_retun_policy}
        print(dic_informetion)
        list_ofdress.append(dic_informetion)
        break
    return list_ofdress
scrapping_details()

