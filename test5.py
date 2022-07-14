from helium import *
from selenium import webdriver
from lxml import html
import csv
from time import sleep
from itertools import zip_longest
driver=webdriver.Chrome()
title=[]
price=[]
raiting=[]
manufacturer=[]
link=[]
page=[]
for pn in range(1,10):
    driver.get('https://www.aliexpress.com/wholesale?trafficChannel=main&d=y&CatId=0&SearchText=speaker&ltype=wholesale&SortType=default&page={}'.format(pn))
    sleep(1)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    tree=html.fromstring(driver.page_source)
    #print(tree)
    i=0
    sleep(1)


    for product_tree in tree.xpath('//div[@class="JIIxO"]'):
        title.append(product_tree.xpath('.//h1[@class="_3eC3x"]/text()'))
        price.append(product_tree.xpath('.//div[@class="_13_ga _37W_B"]/span/text()'))
        link.append(product_tree.xpath('//a[@class="_3KNwG _2f4Ho"]/@href'))
        raiting.append(product_tree.xpath('.//span[@class="ZwoRt"]/text()'))
        manufacturer.append(product_tree.xpath('.//a[@class="ox0KZ"]/text()'))
        page.append(pn)
       
        #print(price)
       
#y=''.join(title[0])
#z=y.split(",")
#print(z[0])
flist=[title,price,link,manufacturer,raiting,page]
#print(len(title))
#print(len(price))

exp=zip_longest(*flist)
with open("project.csv", "w",newline="",encoding="utf-8") as myfile:
    write=csv.writer(myfile)
    write.writerow(["Item name","Itemprice","link","item manufacturer","item rating","Page No."])
    write.writerows(exp)
        

