import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get("https://hrhs.atlas-hub.co.uk/report")
    time.sleep(10)

    username_email_field = driver.find_element(By.ID, "signInName")
    password_field = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "next")

    username_email_field.clear()
    username_email_field.send_keys("mismgr@venus.sg")
    time.sleep(5)

    password_field.clear()
    password_field.send_keys("$Pasword$123!!")
    time.sleep(5)

    login_btn.click()
    time.sleep(5)

except Exception as e:
    print(e)
finally:
    driver.close()

