from selenium import webdriver    #open webdriver for specific browser
from selenium.webdriver.common.keys import Keys   # for necessary browser action
from selenium.webdriver.common.by import By    # For selecting html code
import time
import requests
from bs4 import BeautifulSoup
driver = webdriver.Firefox(executable_path='D:\Users\Nishanth18\Desktop\geckodriver')
driver.get("https://www.snapdeal.com/search?keyword=smartphones&santizedKeyword=&catId=&categoryId=0&suggested=true&vertical=&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy")
#elm = driver.find_element_by_tag_name('html')
for i in range(0,6):
    for j in range(0,3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
    next = driver.find_element_by_css_selector('#see-more-products')
    next.click()
html = driver.page_source
page = BeautifulSoup(html,"html.parser")
var1 ,var2,var3,var4 = [],[],[],[]
#title
all_title = page.find_all("p",class_="product-title")
for ptitle in all_title:
    var1.append(ptitle.text)
#price
all_price = page.find_all("span",class_="lfloat product-price")
for price in all_price:
    var2.append(price.text)
#link
#print len(all_price)
lvar = []
all_links = page.find_all("a",class_="dp-widget-link noUdLine")
for link in all_links:
    lvar.append(link['href'])
for i in range(len(lvar)):
    if i % 2 == 0:
        var3.append(lvar[i])
#print len(var3),len(var2),len(var1)
with open("Snap_data.txt", "a") as myfile:
    for i in range(len(var3)):
        myfile.write(var1[i] + "*" + var2[i] + "*" + var3[i] + "\n")
#rating
'''
all_stars = page.find_all('div',class_="filled-stars")
for stars in all_stars:
    var4.append(stars['style'])
'''

