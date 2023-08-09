import os
import sys
import urllib.parse
import urllib.request
import ssl
import csv_to_dataframe

ssl._create_default_https_context = ssl._create_unverified_context

client_id = "D507KngjGElfvs6kHu9Z"
client_secrect = "EPQNZ2cmSZ"
encText = urllib.parse.quote(csv_to_dataframe.text1)
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secrect)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200) :
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

'''

한 -> 영 변역 : data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"

언어감지 : data = "query=" + encQuery
url = "https://openapi.naver.com/v1/papago/detectLangs"

영 -> 한 번역: data = 없음
url = "https://openapi.naver.com/v1/krdict/romanization?query=" + encText

'''