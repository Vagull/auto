from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://elevator-qa.au.alterosmart.dev/login")
time.sleep(3)
search_box = driver.find_element(By.ID, 'username')
search_box.send_keys("n.safronov")
search_password = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/form/div[2]/label/div/input')
search_password.send_keys("gfcrelfndfhm1")
search_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/form/div[4]/button')
search_button.click()
time.sleep(2)
search_lk = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]')
search_lk.click()
time.sleep(1)
search_leftmenu = driver.find_element(By.XPATH, '/html/body/div[4]')
search_leftmenu.click()
time.sleep(2)



driver.close()
driver.quit()