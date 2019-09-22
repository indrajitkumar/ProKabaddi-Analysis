# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import numpy as np


url = "https://www.prokabaddi.com/players/maninder-singh-profile-143"

web_r = requests.get(url)
websoup = BeautifulSoup(web_r.text, 'html.parser')

driver = webdriver.Firefox()
driver.get(url)
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(web_r.text, 'html.parser')


wait = WebDriverWait(driver, 10)

element = driver.find_element_by_xpath("//div[@class='si-tab si-profile-tabs']").click();
wait

csvfile = open("test.csv", "wt", newline='')
writer = csv.writer(csvfile)

lsi = []
try:
   datas = driver.find_elements_by_class_name("si-tbl-data")
   for post in datas:
#       print(post.text)
       csvrow = []
       csvrow.append(post.text)
#       lsi =  np.array_split(csvrow, 7)
       print(csvrow)
       writer.writerow(csvrow)
finally:
    csvfile.close                       
    
#print(str(csvrow))