import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(executable_path='D:\Users\Nishanth18\Desktop\geckodriver')
driver.get("http://www.shopclues.com/search?q=smartphones&sc_z=4444&z=1")
#driver.execute_script("window.scrollTo(0, 2600);")
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
for i in range(40):
    time.sleep(5)
    next = driver.find_element_by_css_selector('#moreProduct')
    next.click()
html = driver.page_source
var1,var2,var3,var4 = [],[],[],[]
page = BeautifulSoup(html,"html.parser")
all_title = page.find_all("div",class_="column col3")
for i in range(0,len(all_title)):
    var1.append(all_title[i].find('h3').text)
all_price = page.find_all("span",class_="p_price")
for i in range(0,len(all_price)):
    var2.append(all_price[i].text)
all_links = page.find_all("div",class_="column col3")
for i in range(0,len(all_links)):
    link = all_links[i].find('a')
    var3.append(link['href'])
print len(all_title)
with open("Shopclues_data.txt", "a") as myfile:
    for i in range(len(var3)):
        myfile.write(var1[i] + "*" + var2[i] + "*" + var3[i] + "\n")
time.sleep(300)
driver.quit()