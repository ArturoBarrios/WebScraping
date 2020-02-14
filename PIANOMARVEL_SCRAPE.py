from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re


import time
class PIANOMARVEL:
    def __init__(self,driver):
        self.driver = driver

    #gather hyper links from main drop page
    def gather_hyper_links(self):
        hyperlinks = []
        elems = self.driver.find_elements_by_xpath("//a[@href]")
        count = 0
        for elem in elems:
            href = str(elem.get_attribute("href"))
            if "https://pianomarvel.com/sheet-music" in href:
                #print(elem.get_attribute("href"))
                hyperlinks.append(str(elem.get_attribute("href")))
                count+=1
        return hyperlinks

    #returns dictionary of links to songs with corresponding grade
    def gather_rows(self):
        result = dict()
        table_id = self.driver.find_element(By.ID, 'datatable')
        rows = table_id.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
        for row in rows:      
            col = row.find_elements(By.TAG_NAME, "td")
            if len(col)==7:
                elements = col[0].find_elements(By.TAG_NAME,"a")
                link = elements[0].get_attribute("href")
                grade = int(col[3].text)
                result[link] = grade
        print(result)
        return result
    #next page
    def nextPage(self):
        next = self.driver.find_element_by_id('datatable_next')
        print("next: ",next)
        next.click()

    def close_tab(self,tab_index):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[tab_index])
    