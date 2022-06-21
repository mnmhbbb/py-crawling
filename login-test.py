from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

# 불필요한 에러 메시지 없애기
# chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

# 크롬 드라이버 자동 설치
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소로 이동
driver.implicitly_wait(5) # 웹페이지 로딩 기다리기
driver.maximize_window() # 화면 최대화
driver.get('https://n09b2b.co.kr/intro/member.html?returnUrl=%2Fproduct%2Flist.html%3Fcate_no%3D479%26page%3D2')

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, '#member_id')
id.click()
id.send_keys('idid')
# 자동입력방지:
# pyperclip.copy('idid')
# pyautogui.hotkey('command', 'v')
time.sleep(2)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, '#member_passwd')
pw.click()
pw.send_keys('pwpw')
# 자동입력방지:
# pyperclip.copy('pwpw')
# pyautogui.hotkey('command', 'v')
time.sleep(2)

# 로그인 버튼
login_btn = driver.find_element(By.CSS_SELECTOR, '.btn')
login_btn.click()