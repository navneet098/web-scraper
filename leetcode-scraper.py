import time
from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome()

driver.get("https://leetcode.com/tag/dynamic-programming/")
time.sleep(1)
html=driver.page_source
html=html.encode('cp1252', errors='replace').decode('cp1252')
soup=BeautifulSoup(html,'html.parser')
# print(soup)
all_ques_td=soup.find_all("td",{"label":"Title"})
print(len(all_ques_td))
all_ques_diff=soup.find_all("td",{"label":"Difficulty"})
#  all_ques=[]
# urls=[]
title=[]
diff=[]
#  for ques in all_ques_tr:
#      all_ques.append(ques.findAll("tr")[0].find("a"))

for ques in all_ques_diff:
    diff.append(ques.findAll("span")[0].text)

for ques in all_ques_td:
    #  urls.append(ques['href'])
     title.append(ques['value'])
# # print(urls[0])

with open("lc_difficulty.txt", "w+") as f:
     f.write('\n'.join(diff))

with open("lc_titles.txt", "w+") as f:
     f.write('", \n"'.join(title))
