
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs
import warnings

slang_title = []
slang_description = []
dictionary_numbers = [1, 2, 5, 6, 8, 11, 12, 14, 18]

url = "https://open-pro.dict.naver.com/_ivo/search?searchVal=신조어"
browser = webdriver.Safari()
browser.get(url)

sum = 0
n = 2
total_n = 2
slang_page = 0
sum_dictionary = 1
dictionary_page = 2
next_dictionary = 1

'''
card = browser.find_element(By.CLASS_NAME, "title-num").text
전체 사전집 크롤링
'''

while(1) :
    time.sleep(3)
    if sum_dictionary == len(dictionary_numbers) : break
    if next_dictionary > 20 :
        cur_css = '#content > div.section-main > div.dict > div.page > button:nth-child({})'.format(dictionary_page)
        button = browser.find_element(By.CSS_SELECTOR, cur_css)
        button.click()
        dictionary_page += 1
        next_dictionary = 0 
        
    else :
        cur_css = '#content > div.section-main > div.dict > ul.dict-list.pc > li:nth-child({})'.format(dictionary_numbers[next_dictionary - 1])
        button = browser.find_element(By.CSS_SELECTOR, cur_css)
        button.click()
        time.sleep(3) 

    while(1) :
        pagesize = browser.find_elements(By.XPATH,'//*[@id="content"]/div[2]/div[4]/div[3]/button[@class="page-btn"]')
        next = browser.find_elements(By.CLASS_NAME, "next-btn")

        if len(next):
            time.sleep(3)
            sum += 10
            slang_page += 1
            button = browser.find_element(By.CSS_SELECTOR,'#content > div.section-main > div.word > div.page > button.next-btn')
            button.click()

        else :
            sum += len(pagesize) + 1
            break

    if slang_page > 0 :
        browser.find_element(By.CSS_SELECTOR,'#content > div.section-main > div.word > div.page > button.prev-btn' ).click()
        slang_page -= 1

    while(True) :
        time.sleep(3)
        titles = browser.find_elements(By.CLASS_NAME , "card-title")
        descriptions = browser.find_elements(By.CLASS_NAME, "card-desc__text")

        for title in titles:
            slang_title.append(title.text)

        for description in descriptions:
            slang_description.append(description.text)

        if n == 11 :
            cur_css = '#content > div.section-main > div.word > div.page > button.next-btn'
            n = 2
        
        elif total_n == sum+1 : 
            browser.get(url)
            sum = 0
            n = 2
            total_n = 2
            slang_page = 0
            break

        else :
            cur_css = '#content > div.section-main > div.word > div.page > button:nth-child({})'.format(n)

        button = browser.find_element(By.CSS_SELECTOR, cur_css)
        button.click()
        n += 1
        total_n +=1

    sum_dictionary += 1
    next_dictionary += 1
    data = {"title" : slang_title, "description" : slang_description}
    df = pd.DataFrame(data)
    df.to_csv("test3.csv", encoding = "utf-8-sig")

time.sleep(10)
browser.close()