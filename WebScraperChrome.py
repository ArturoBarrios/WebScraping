from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from DROP_SCRAPE import DROP
from EBAY_SCRAPE import EBAY

import time
driver = webdriver.Chrome()
driver.get("https://drop.com/?origin=%2Fhome")

delay = 3 # seconds

#sign in to drop website
drop = DROP(driver)
ebay = EBAY(driver)
drop.login()
time.sleep(2)
#gather hyper links to purchasable items
hyperlinks = drop.gather_hyper_links()



index = 0
# #go to hyperlink and gather price information
for hyperlink_element in hyperlinks:
    if index==0:
        #open new hyperlink
        drop.open_new_drop_tab(hyperlinks[2])
        #price:    wdio__price Text__text__PazWx Text__type--price__1mumP
        time.sleep(3)
        price = drop.get_new_price()
        if price is not None:
            print("Price: ",price,"\n")
            item_name = drop.get_item_name()
            #print("Item Name: ",item_name)
            retail_price = drop.get_retail_price()
            print("Retail Price: ",retail_price,"\n")
            rating_count = drop.get_rating_count()
            print("Rating Count: ",rating_count,"\n")
            units_sold = drop.get_units_sold()
            print("Units Sold: ",units_sold,"\n\n\n")
            drop.close_tab(-1)
            time.sleep(1)
            #go to ebay tab
            ebay.open_ebay_tab()
            time.sleep(5)
            #login
            ebay.login()
            time.sleep(2)
            #search for item
            ebay.search_item(item_name)
            time.sleep(4)
            ebay.get_item_price(5)
            time.sleep(2)
            ebay.get_item_quality(5)
            time.sleep(2)
            ebay.get_item_rating(5)
            time.sleep(2)
            ebay.get_rating_count(5)
            # ebay.get_item_quality(5)

            #close tab
            # ebay.close_tab(-1)
            # time.sleep(2)

    #print("\n\n\n\n\n")

    index+=1
