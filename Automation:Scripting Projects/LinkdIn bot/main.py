from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


url = "https://www.linkedin.com/jobs/search/?currentJobId=3687787550&f_AL=true&keywords=python%20developer&refresh=true"

driver = webdriver.Chrome()
driver.get(url=url)
time.sleep(5)
sign_in_button = driver.find_element(By.CSS_SELECTOR, 'div .cta-modal__primary-btn')
sign_in_button.click()
email = driver.find_element(By.ID, "username")
email.send_keys(EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
driver.find_element(By.CLASS_NAME, "btn__primary--large").click()
job_list = driver.find_elements(By.CLASS_NAME, "disabled")
print(len(job_list))
for job in job_list:
    job.click()

time.sleep(1000)




