import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)


# open nwpu
browser.get('https://uis.nwpu.edu.cn/cas/login?service=https://ecampus.nwpu.edu.cn/')
browser.maximize_window()

# login
username = browser.find_element(By.ID, "username")
username.send_keys(USERNAME)
time.sleep(1)
password = browser.find_element(By.ID, "password")
password.send_keys(PASSWORD)
browser.find_element(By.NAME, "submit").click()
time.sleep(1)

browser.get('https://yqtb.nwpu.edu.cn/wx/ry/jrsb_xs.jsp')
browser.refresh()
time.sleep(1)

browser.find_element(By.XPATH, "//div[@class='weui-btn-area']").click() # 提交填报信息
browser.find_element(By.XPATH, "//label[@class='weui-cell weui-cell_active weui-check__label']").click() # 已核实 
browser.find_element(By.ID, "save_div").click() # 确认提交
time.sleep(1)
    
browser.quit()
