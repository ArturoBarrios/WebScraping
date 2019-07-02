from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://drop.com/?origin=%2Fhome")

delay = 3 # seconds

#open sign up modal
login_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "splash__sign_in_button ")))
login_button.click()

#wait for all buttons to load
time.sleep(5)
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "button--emulate-continue-as")))
#send username and password to login
login_button = None
try:
    driver.find_element_by_name("username").send_keys("arturobarrios357@gmail.com")
except:
    driver.find_element_by_name("email").send_keys("arturobarrios357@gmail.com")
driver.find_element_by_name("password").send_keys("Ruforufo4$")
try:
    login_button = driver.find_element(By.XPATH, '//button[text()="Continue"]')
except:
    login_button = driver.find_element(By.XPATH, '//button[text()="Log in"]')
login_button.click()

#go to shop link
time.sleep(5)
driver.find_element_by_link_text("SHOP").click()
time.sleep(5)
#scroll to bottom
SCROLL_PAUSE_TIME = 0.5
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


elems = driver.find_elements_by_xpath("//a[@href]")
count = 0
for elem in elems:
    href = str(elem.get_attribute("href"))
    if "buy" in href and "discussion" not in href :
        count+=1
        print(elem.get_attribute("href"))
print(count)
