import time

from selenium import webdriver


browser = webdriver.Chrome()

# 1. 네이버 이동
browser.get('http://naver.com')

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name('link_login')
elem.click()

# 3. 아이디, 패스워드 입력
browser.find_element_by_id('id').send_keys('naver_id')
browser.find_element_by_id('pw').send_keys('password')

# 4. 로그인 버튼 클릭
browser.find_element_by_id('log.login').click()

time.sleep(3)

# 5. id를 새로 입력
# browser.find_element_by_id('id').send_keys('my_id')
browser.find_element_by_id('id').clear()
browser.find_element_by_id('id').send_keys('my_id')

# 네이버 로그인 우회하기
# https://jaeseokim.github.io/Python/python-Selenium%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%9B%B9-%ED%81%AC%EB%A1%A4%EB%A7%81-Naver-login-%ED%9B%84-%EA%B5%AC%EB%8F%85-Feed-%ED%81%AC%EB%A1%A4%EB%A7%81/

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit()  # 전체 브라우저 종료