from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re


import time
class EBAY:
    def __init__(self,driver):
        self.driver = driver

    #open new drop tab
    def open_ebay_tab(self):
        self.driver.execute_script("window.open('');")
        time.sleep(3)
        Window_List = self.driver.window_handles
        self.driver.switch_to_window(Window_List[-1])
        self.driver.get("https://www.ebay.com/")


    # #open new drop tab
    # def open_new_drop_tab(self,hyperlink):
    #     self.driver.execute_script("window.open('');")
    #     time.sleep(3)
    #     Window_List = self.driver.window_handles
    #     self.driver.switch_to_window(Window_List[-1])
    #     self.driver.get(hyperlink)

    #close tab
    def close_tab(self,tab_index):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[tab_index])

    #login to ebay
    def login(self):
        login = self.driver.find_elements_by_xpath("//*[contains(text(), 'Sign in')]")
        login[0].click()
        #send username and password to login
        login_button = None
        try:
            self.driver.find_element_by_name("userid").send_keys("arturobarrios0714@gmail.com")
        except:
            print("no login input found")
        try:
            self.driver.find_element_by_name("pass").send_keys("Ruforufo0714")
        except:
            print("no password input found")
        try:
            login_button = self.driver.find_element_by_id('sgnBt')
        except:
            print("no sign in button found")
        login_button.click()

    #search for item
    def search_item(self,item_name):
        #input item name
        try:
            self.driver.find_element_by_name("_nkw").send_keys(item_name)
        except:
            print("no search bar found")
        #search
        try:
            search_button = self.driver.find_element_by_id('gh-btn')
        except:
            print("no search button found")
        search_button.click()
