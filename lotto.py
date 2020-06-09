
# selenium 임포트
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
# chrome_options.add_argument("--headless")

# webdriver 설정(Chrome, Firefox 등) - Headless 모드
browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe', options=chrome_options)

# webdriver 설정(Chrome, Firefox 등) - 일반 모드
# browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe')

# 크롬 브라우저 내부 대기
browser.implicitly_wait(5)

# 브라우저 사이즈
browser.set_window_size(1920, 1280)  # maximize_window(), minimize_window()

# 페이지 이동
browser.get('https://dhlottery.co.kr/user.do?method=login')

browser.find_element_by_name('userId').clear()

browser.find_element_by_name('password').clear()

browser.find_element_by_name('userId').send_keys('wkdals1474')

browser.find_element_by_name('password').send_keys('jangmin1004!')


# 로그인 버튼 클릭
WebDriverWait(browser, 2) \
    .until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.box_login .btn_common'))).click()

# 2초간 대기
time.sleep(2)

# 팝업창 오픈시, 메인 윈도우창과, 서브 윈도우 창을 구분해주기 위해 선언
main_window_handle = None
while not main_window_handle:
    main_window_handle = browser.current_window_handle
browser.find_element_by_xpath(u'//a[text()="복권구매"]').click()

sub_window_handle = None
while not sub_window_handle:
    for handle in browser.window_handles:
        if handle != main_window_handle:
            sub_window_handle = handle
            break

browser.switch_to.window(sub_window_handle)

# 복권구매 클릭 클릭
WebDriverWait(browser, 2) \
    .until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#notshow'))).click()

# 2초간 대기
time.sleep(2)

sub_window_handle2 = None
while not sub_window_handle2:
    for handle in browser.window_handles:
        if handle != main_window_handle:
            sub_window_handle2 = handle
            break

browser.switch_to.window(sub_window_handle2)

# 복권구매 클릭 클릭
WebDriverWait(browser, 2) \
    .until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#notshow'))).click()

time.sleep(2)

browser.switch_to.window(main_window_handle)

# browser.switch_to.window(main_window_handle) #or driver.switch_to_default_content()



# 복권구매 클릭 클릭
WebDriverWait(browser, 2) \
    .until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.gnbNav ul .gnb1 a'))).click()

# 2초간 대기
time.sleep(2)

# 로또구매 클릭 클릭
WebDriverWait(browser, 2) \
    .until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.gnb1_1 > a'))).click()

# 2초간 대기
time.sleep(2)

browser.switch_to.alert.accept()

# 번호 클릭
WebDriverWait(browser, 2) \
    .until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.game-645-wrap .game-645-content > .select-number .ways #divWay2Buy1 > .paper > #checkNumGroup > label[for="check645num8"]'))).click()

# 2초간 대기
time.sleep(1)




# 브라우저 종료
browser.quit()
