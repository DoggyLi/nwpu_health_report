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
browser = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)


# open nwpu
# browser.get('https://uis.nwpu.edu.cn/cas/login?service=https://ecampus.nwpu.edu.cn/')
browser.get('https://yqtb.nwpu.edu.cn/wx/ry/jrsb_xs.jsp')
browser.maximize_window()
time.sleep(1)
# # login
browser.find_element(By.XPATH, "/html/body/main/div/div/div[2]/div[3]/div/div[2]/div[3]/div/div/div[1]/ul/li[3]").click()
username = browser.find_element(By.ID, "username").click()
username.send_keys(USERNAME)
password = browser.find_element(By.ID, "password").click()
password.send_keys(PASSWORD)
browser.find_element(By.XPATH, "/html/body/main/div/div/div[2]/div[3]/div/div[2]/div[3]/div/div/div[2]/div/form/div[4]/div/input[6]").click()

# browser.get('https://yqtb.nwpu.edu.cn/wx/ry/jrsb_xs.jsp')
browser.refresh()
# time.sleep(1)
print(browser.current_url)


# browser.find_element(By.XPATH, "//a[@class='weui-btn weui-btn_primary']").click()# 提交填报信息
# <a href="javascript:go_subfx();" style="" class="weui-btn weui-btn_primary">提交填报信息</a>
# browser.find_element(By.XPATH, "//label[@class='weui-cell weui-cell_active weui-check__label']").click() # 已核实 
# browser.find_element(By.ID, "save_div").click() # 确认提交
# time.sleep(1)
    
browser.quit()
