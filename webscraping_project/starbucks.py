from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.starbucks.co.kr/menu/drink_list.do'

browser = webdriver.Chrome()
browser.get(url)

elems = browser.find_elements_by_css_selector('#container > div.content > div.product_result_wrap.product_result_wrap01 > div > dl > dd:nth-child(2) > div.product_list > dl > dd:nth-child(2) > ul > li')
for e in elems:
    print(e.text)

# elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#container > div.content > div.product_result_wrap.product_result_wrap01 > div > dl > dd:nth-child(2) > div.product_list > dl > dd:nth-child(2) > ul > li:nth-child(1)')))
# print(elem.text)

browser.quit()