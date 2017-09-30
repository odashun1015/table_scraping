from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas
import time
#PhantomJSのWebDriverオブジェクトを作成する
driver = webdriver.PhantomJS()
url='https://roote.ekispert.net/ja/timetable'
name=input()
driver.get(url)#open top menu
#input station_name in textbox
input_element = driver.find_element_by_name('station')#ID
input_element.send_keys(name)
input_element.send_keys(Keys.RETURN)
#show direction of line list
element=driver.find_elements_by_partial_link_text("方面")
list=[]
[list.append([name,element[i].text,element[i].get_attribute('href')]) for i in range(len(element))]
print(list)
