import time
from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome()
driver.get("https://www.codechef.com/practice/dynamic-programming")
time.sleep(1)
html=driver.page_source
html=html.encode('cp1252', errors='replace').decode('cp1252')
soup=BeautifulSoup(html,'html.parser')
# print(soup)
all_ques_tr=soup.find_all("tr",{"class":"_tableBody_15k3c_322"})
print(len(all_ques_tr))

all_ques=[]
urls=[]
title=[]
for ques in all_ques_tr:
    all_ques.append(ques.findAll("td")[0].find("a"))

for ques in all_ques:
     urls.append(ques['href'])
     title.append(ques.text)
# print(urls[0])

with open("cc_urls.txt", "w+") as f:
     f.write('\n'.join(urls))

with open("cc_titles.txt", "w+") as f:
     f.write('", \n"'.join(title))
