# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 10:18:09 2020

@author: cis-user
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# r = requests.get("https://udn.com/news/story/7321/5018383?from=udn_ch2_menu_v2_main_index")
r = requests.get("https://udn.com/news/story/121687/5018971")
r.encoding = "utf8"

with open('html.txt', "w", encoding="utf8") as fp:
    # print(r.text,file=fp)                                 ##可用print，也可用write
    fp.write(r.text)
    
with open('html.txt', "r", encoding="utf8") as fp2:
    r2=fp2.read() 
    
page_source = r.text
page_source2 = page_source.split('\n')

soup = BeautifulSoup(r.text, "lxml")

####################################第一種#######################################
# tag_div=soup.find_all('div',class_="article-content__paragraph")
# print(tag_div)
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# for a in tag_div:
#     print(a.text)
tag_div=soup.find_all('article',class_="article-content")
print(tag_div)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for a in tag_div:
    print(a.text)
    
    
# import csv
# f=open('data.csv','w')
# w=csv.writer(f)


####################################第二種#######################################

# search_span=soup.select("body > main > div > section.wrapper-left.main-content__wrapper > section > article > div > section.article-content__editor")

# search_span2=soup.select("div > ul > li > a")


# print(soup.prettify())

# r.test.to_csv('GetAllStock.csv',encoding='utf-8-sig')