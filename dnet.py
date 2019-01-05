import time as t
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import io
import pandas as pd
import csv

path = "C:\\Users\\Yasir\\Downloads\\chromedriver.exe"
driver = webdriver.Chrome(path)

url = ""
data = []

for _ in range(48):
    driver.get(url)


    html = driver.page_source
    html = soup(html)

    #Check if the next page exists 
    url = 0 
    url = html.find("li",class_ = 'ipsPagination_next').find('a')['href']

    all_threads = html.find_all('div', class_ = 'ipsDataItem_main')

    #Opens all the thread on a page 

    links = []
    for thread in all_threads:
        link = thread.find('a')
        links.append(link['href'])

    #Op from all tags
    for link in links:
        driver.get(link)
        driver.implicitly_wait(5)    
        html = driver.page_source
        html = soup(html)
        comment = html.find('div', class_ = 'cPost_contentWrap ipsPad').text.replace("\n"," ").strip()
        data.append(comment)
    

import pandas as pd
X = pd.DataFrame(data,columns = ['Data'])
X.to_csv("Mental Health_dnet.csv")

driver.close()

    







    
    
        