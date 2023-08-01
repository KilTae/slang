
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs
import warnings


slangtitle = []
slangdescription = []

url = "https://open-pro.dict.naver.com/_ivo/search?searchVal=신조어"



browser = webdriver.Safari()
browser.get(url)
sum = 0
num = 2
sumnum = 2
nextpage = 0
bububu = 1
page = 2

card = browser.find_element(By.CLASS_NAME, "title-num").text
bubu = 1
while(1) :
    time.sleep(3)
    if bububu == int(card) : break
    if bubu > 20 :
        cur_css = '#content > div.section-main > div.dict > div.page > button:nth-child({})'.format(page)
        bubu = 0 
        button = browser.find_element(By.CSS_SELECTOR, cur_css)
        button.click()
        page += 1
        
    else :
        cur_css = '#content > div.section-main > div.dict > ul.dict-list.pc > li:nth-child({})'.format(bubu)
        button = browser.find_element(By.CSS_SELECTOR, cur_css)
        button.click()
        time.sleep(3)
        browser.back()
    

    bububu += 1
    bubu += 1



'''
while(1) :
    pagesize = browser.find_elements(By.XPATH,'//*[@id="content"]/div[2]/div[4]/div[3]/button[@class="page-btn"]')
    next = browser.find_elements(By.CLASS_NAME, "next-btn")

    if len(next):
        time.sleep(3)
        sum += 10
        nextpage += 1
        button = browser.find_element(By.CSS_SELECTOR,'#content > div.section-main > div.word > div.page > button.next-btn')
        button.click()

    else :
        sum += len(pagesize) + 1
        break

if nextpage > 0 :
    browser.find_element(By.CSS_SELECTOR,'#content > div.section-main > div.word > div.page > button.prev-btn' ).click()
    nextpage -= 1
    
    
while(True) :
    time.sleep(3)

    titles = browser.find_elements(By.CLASS_NAME , "card-title")
    descriptions = browser.find_elements(By.CLASS_NAME, "card-desc__text")

    for title in titles:
        slangtitle.append(title.text)

    for description in descriptions:
        slangdescription.append(description.text)

    if num == 11 :
        cur_css = '#content > div.section-main > div.word > div.page > button.next-btn'
        num = 2
    
    elif sumnum == sum+1 : break

    else :
        cur_css = '#content > div.section-main > div.word > div.page > button:nth-child({})'.format(num)

    button = browser.find_element(By.CSS_SELECTOR, cur_css)
    button.click()
    num += 1
    sumnum +=1
    print(sumnum)



data = {"title" : slangtitle, "description" : slangdescription}
df = pd.DataFrame(data)
print(df)

df.to_csv("test3.csv", encoding = "utf-8-sig")

'''
time.sleep(10)

browser.close()