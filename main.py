from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service('c:/Users/Александр/Desktop/chromedriver_win32.zip/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
time.sleep(1)
driver.set_window_size(1366,768)
driver.find_element(By.XPATH,"//*[@id='login-button']").click()
driver.find_element(By.XPATH,"//*[@id='login-otp-button']").click()
driver.find_element(By.XPATH,"//*[@id='accounts-index']").click()
driver.find_element(By.XPATH,"//*[@id='contentbar']/form/div/a").click()
driver.find_element(By.XPATH,"//*[@id='new-account-form']/div[2]/div/div/div/label/p/span").click()
driver.find_element(By.XPATH,"//*[@id='submit']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='logout-button']/span").click()
time.sleep(2)


