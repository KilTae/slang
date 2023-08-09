import numpy as np
import os
import pandas as pd
from kiwipiepy import Kiwi
import sys
import urllib.parse
import urllib.request
import ssl

data = pd.read_csv("slangs.csv", sep = ";",encoding='utf-8-sig')
kiwi=Kiwi()
for i in data['title']:
  kiwi.add_user_word(i.replace(" ",""),tag='NNG',score=0.0)
text1="알잘딱깔센 했어야지"
kiwi.tokenize(text1)

def extract_noun(text):
  result = kiwi.tokenize(text1)
  for token in result :
    if token.tag in ['NNG']:
      yield token.form

nouns = list(extract_noun(text1))
title_list1=[]
title_list = data['title'].values.tolist()
for i in title_list:
  i=i.strip()
  title_list1.append(i)

for noun in nouns :
  if noun in title_list1 :
    indx = title_list1.index(noun)
    description = data.iloc[indx].description
    text1 = text1.replace(noun, description)
    print(text1)

