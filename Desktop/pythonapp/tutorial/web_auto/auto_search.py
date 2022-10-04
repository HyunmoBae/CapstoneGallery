from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('C:/chromedriver.exe')
browser.get('https://www.naver.com')

# browser.implicitly_wait(10) #로딩 후 10초 대기
browser.maximize_window() #화면 최대화
browser.find_element(By.CSS_SELECTOR, "#NM_FAVORITE > div.group_nav > ul.list_nav.type_fix > li:nth-child(5) > a")
browser.click()

search = browser.find_element(By.CSS_SELECTOR, "#__next > div > div.header_header__24NVj > div > div > div._gnb_header_area_150KE > div > div._gnbLogo_gnb_logo_3eIAf > div > div._gnbSearch_gnb_search_3O1L2 > form > fieldset > div._gnbSearch_inner_2Zksb > div._searchInput_search_input_QXUFf > input")
search.click()

search.send_keys("노트북")
search.send_keys(Keys.ENTER)