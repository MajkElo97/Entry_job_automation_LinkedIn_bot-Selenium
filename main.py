from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

login = "your login here"
passw = "your password here"

chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(service=Service(chrome_driver_path))

url = "https://www.linkedin.com/jobs/search/?currentJobId=3368501613&f_LF=f_AL&geoId=90009829&keywords=python%20developer&location=Katowice%20i%20okolice&refresh=true"
driver.get(url=url)
driver.maximize_window()

button_log = driver.find_element(by=By.LINK_TEXT, value="Zaloguj się")
button_log.click()
email = driver.find_element(by=By.NAME, value="session_key")
email.send_keys(login)
password = driver.find_element(by=By.NAME, value="session_password")
password.send_keys(passw)
password.submit()
time.sleep(3)

job_list = driver.find_elements(by=By.CSS_SELECTOR, value='ul.scaffold-layout__list-container li.jobs-search-results__list-item')
print(len(job_list))
scroll_cor = 100
for job in job_list:
    time.sleep(2)
    job.click()
    time.sleep(2)
    job.click()
    time.sleep(2)
    button_save_text = driver.find_element(by=By.CSS_SELECTOR, value='.jobs-save-button span').text
    button_save = driver.find_element(by=By.CSS_SELECTOR, value='.jobs-save-button')
    if button_save_text == "Zapisz":
        button_save.click()
time.sleep(5)
driver.quit()
