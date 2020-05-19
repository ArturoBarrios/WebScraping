from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PIANOMARVEL_SCRAPE import PIANOMARVEL
from PROCESS import ProcessMidiFiles
import unicodedata
import time
import os

#finds downloadable url in html body
def findURL(html_string):
    print "type of string: ", type(html_string)
    i = 0
    Found = False
    #find last characters of url(.'mid')
    while i<len(html_string) and not Found:
        if html_string[i:i+4] == ".mid":
            print("no wayyyyyyy!    ", html_string[i-10:i])
            Found = True
            i+=4
        else:
            i+=1
    Found = False
    j = i
    while j>0 and not Found:
        if html_string[j-12:j]=='#midi-player':
            print("wtff bro")
            Found = True
        else:
            j-=1 
    result = str(html_string[j+4:i])
    start = str("https://pianomarvel.com")
    result = start+result
    print "resulttttttttt: "+result
    for char in result:
        print("charr: ",result)

    return result





def open_window(html_string):
    driver.execute_script("window.open('');")
    time.sleep(3)
    Window_List = driver.window_handles
    driver.switch_to_window(Window_List[-1])
    driver.get(html_string)




driver = webdriver.Chrome('chromedriver')
driver.get("https://pianomarvel.com/music-library")
delay = 3 # seconds
#initialize Piano Marevl Scraper
piano_marvel = PIANOMARVEL(driver)
time.sleep(4)
i = 0

#i<number of pages
while i<1:
    #grab all songs on page
    rows = piano_marvel.gather_rows()
    #rename downloaded files
    process = ProcessMidiFiles(rows)
    
    piano_marvel.nextPage()
    time.sleep(1)
    print "rows for page: "+str(i)
    print rows
    #find each rows corresponding download link
    j = 0
    for hyperlink,grade in rows.items():
        print(hyperlink,"   ",grade)
        #if j<1:
        #get hyperlink and grade
        open_window(hyperlink)
        time.sleep(4)
        html = driver.page_source
        html_string = unicodedata.normalize('NFKD', html).encode('ascii','ignore')
        downloadable_url = findURL(html_string)
        print("downloadablee url: ",downloadable_url)
        #close tab
        piano_marvel.close_tab(-1)
        #open new tab#this downloads a .mid file
        open_window(downloadable_url)
        #rename downloaded midi file
        time.sleep(4)
        process.rename_files("/Users/arturobarrios/Downloads/",grade)
        #close download tab
        piano_marvel.close_tab(-1)
        # j+=1
    i+=1

# #rename downloaded files
# process = ProcessMidiFiles(rows)
# process.rename_files()
       

