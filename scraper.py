from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_latest_results():
    driver = webdriver.Chrome()
    driver.get("https://www.damangames.bet")
    time.sleep(2)
    
    # Login
    driver.find_element(By.NAME, "mobile").send_keys("7404207375")
    driver.find_element(By.NAME, "password").send_keys("harman12")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(5)

    # Go to Wingo 1-min
    driver.get("https://www.damangames.bet/game/wingo")
    time.sleep(5)

    # Get last 3 numbers
    results = driver.find_elements(By.CLASS_NAME, "result-item")
    last3 = [int(r.text) for r in results[:3]]

    driver.quit()
    return last3
