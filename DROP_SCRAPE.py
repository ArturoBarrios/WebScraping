from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re


import time
class DROP:
    def __init__(self,driver):
        self.driver = driver


    #login to massdrop website
    def login(self):
        #open sign up modal
        login_button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "splash__sign_in_button ")))
        login_button.click()
        #wait for all buttons to load
        time.sleep(2)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "button--emulate-continue-as")))
        #send username and password to login
        login_button = None
        try:
            self.driver.find_element_by_name("username").send_keys("arturobarrios357@gmail.com")
        except:
            self.driver.find_element_by_name("email").send_keys("arturobarrios357@gmail.com")
        self.driver.find_element_by_name("password").send_keys("Ruforufo4$")
        try:
            login_button = self.driver.find_element(By.XPATH, '//button[text()="Continue"]')
        except:
            login_button = self.driver.find_element(By.XPATH, '//button[text()="Log in"]')
        login_button.click()


    #gather hyper links from main drop page
    def gather_hyper_links(self):
        hyperlinks = []
        self.driver.find_element_by_link_text("SHOP").click()
        time.sleep(3)
        #scroll to bottom
        SCROLL_PAUSE_TIME = 0.5
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        i = 0
        while i<3:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            i+=1
        elems = self.driver.find_elements_by_xpath("//a[@href]")
        count = 0
        for elem in elems:
            href = str(elem.get_attribute("href"))
            if "buy" in href and "discussion" not in href :
                #print(elem.get_attribute("href"))
                hyperlinks.append(str(elem.get_attribute("href")))
                count+=1
        return hyperlinks

    #open new drop tab
    def open_ebay_tab(self):
        self.driver.execute_script("window.open('');")
        time.sleep(3)
        Window_List = self.driver.window_handles
        self.driver.switch_to_window(Window_List[-1])
        self.driver.get("https://www.ebay.com/")


    #open new drop tab
    def open_new_drop_tab(self,hyperlink):
        self.driver.execute_script("window.open('');")
        time.sleep(3)
        Window_List = self.driver.window_handles
        self.driver.switch_to_window(Window_List[-1])
        self.driver.get(hyperlink)

    def close_tab(self,tab_index):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[tab_index])

    #get new price
    def get_new_price(self):
        price = None
        try:
            price_element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "wdio__price")))
            print("wdio__price class name found")
            price_content = price_element.get_attribute('innerHTML')
            price = float(price_content.strip()[1:])
        except:
            print("no price found")
        return price

    #get retail price
    def get_retail_price(self):
        price = None
        try:
            price_element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "Text__color--dark-gray__69Ykj")))
            print("Text__color--dark-gray__69Ykj class name found")
            price_content = price_element.get_attribute('innerHTML')
            price = float(price_content.strip()[1:])
        except:
            print("no retail price found")


        return price

    #get rating count
    def get_rating_count(self):
        rating_count = None
        try:
            rating_count_element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "DropPageHeader__reviews_count__3TeJB")))
            rating_count_content = rating_count_element.get_attribute('innerHTML')
            rating_count = int(rating_count_content.strip())
        except:
            print("no rating count found")
        return rating_count

    #get number of units sold
    def get_units_sold(self):
        units_sold = None
        try:
            units_sold_element = self.driver.find_elements_by_xpath("//*[contains(text(), 'Sold')]")
            units_sold_element = units_sold_element[1].get_attribute('innerHTML')
            units_sold = int(re.search(r'\d+', units_sold_element).group())
        except:
            print("no units sold found")
        return units_sold

    #get item item name
    def get_item_name(self):
        item_name = None

        try:
            #Text__text__PazWx Text__type--title-0__2XDay

            item_name_element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "Text__type--title-0__2XDay")))
            item_name_content = item_name_element.get_attribute('innerHTML')
            item_name = item_name_content.strip()
            print("item name: ",item_name)
        except:
            print("couldn't find item name")
        return item_name
