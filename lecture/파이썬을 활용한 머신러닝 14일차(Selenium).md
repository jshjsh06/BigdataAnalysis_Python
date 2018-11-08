# Selenium

## 1. Chromedrive 설치

- https://sites.google.com/a/chromium.org/chromedriver/downloads에서 최신버전을 다운받는다.
- C:\Users\student\Anaconda_src\driver 에 이동시킨다.



## 2. Selenium 이란

- BeautifulSopu 패키지만을 사용하여 크롤링을 할 경우, 모든 웹페이지의 데이터들을 가져오는 것은 아니다.
- 예를들어, 비동기적으로 뒤늦게 웹페이지의 정보를 업데이트하는 경우와 로그인이나 특정권한을 요구하는 웹페이지의 경우가 그럴것이다.
- 이때 필요로 하는 패키지가 바로 셀레늄(Selenium)이며, 별도의 webdriver라는 API를 통해 운영체제에 설치된 브라우저를 제어할 수 있다.
- 즉, 셀레늄을 사용하면 웹페이지상에서 눈에 보이는 모든 데이터를 가져올 수 있다.



### (1) Selenium 설치

- ```python
  from bs4 import BeautifulSoup
  from selenium import webdriver
  from IPython.display import Image
  
  import re
  ```

  - selenium 설치가 안되어 있다면 `! pip install selenium` 명령어로 설치를 별도로 한다.



### (2) selenium 사용

#### 1) selector XPath

- 특정한 링크를 타고 가고 싶다면 개발자 도구 내 해당 링크 항목에 대해 Copy - Copy selector 또는 XPath 를 클릭한다.

#### 2) seleniumhq 홈페이지 이동 및 홈페이지 내 이동

- In [2]:

- driver 폴더를 확인할 것!

  ```python
  # 웹드라이브로 크롬브라우즈 띄운다.
  driver_path = "driver/chromedriver.exe"
  driver = webdriver.Chrome(executable_path=driver_path)
  ```

  In [3]:

  ```python
  url_page = 'http://www.seleniumhq.org/projects/webdriver/'
  driver.get(url_page)
  ```

  In [4]:

  - Copy Selector를 통해 이동

  ```python
  driver.find_element_by_css_selector('#menu_download > a').click()
  ```

  In [5]:

  - images 폴더를 생성할 것!

  ```python
  capture_img = './images/seleniumhq_download.png'
  driver.save_screenshot(capture_img)
  Image(capture_img)
  ```



#### 3) naver 영화 홈페이지 이동

- ### 네이버 크롤링

  In [6]:

  ```python
  url_page = 'https://www.naver.com'
  driver.get(url_page)
  ```

  In [7]:

  - xpath, selector로 하는 방법 같이 표현되어있음

  ```python
  # XQury
  driver.find_element_by_xpath('//*[@id="PM_ID_serviceNavi"]/li[6]/a').click()
  
  # jQuery
  # driver.find_element_by_css_selector('#PM_ID_serviceNavi > li:nth-child(6) > a').click()
  ```

  In [8]:

  ```python
  # 평점&리뷰 1등 페이지로 이동
  driver.find_element_by_css_selector('#review1 > div > a').click()
  ```

  In [9]:

  ```python
  # 리뷰 클릭
  driver.find_element_by_css_selector('#movieEndTabMenu > li:nth-child(6) > a').click()
  ```

  In [10]:

  - 현재 접속해있는 정보를 불러온다.

  ```python
  current_url = driver.current_url
  current_url
  ```

  Out[10]:

  ```python
  'https://movie.naver.com/movie/bi/mi/review.nhn?code=167638'
  ```

  In [11]:

  - code만 따로 추출하기 위해 정규표현식을 사용한다.

  ```python
  # pattern = re.compile("[\d+,?]+")
  pattern = re.compile("\d{6}") # 숫자가 6개인 것을 찾는 정규표현식 정의
  result = pattern.findall(current_url) # 해당 정의를 주소창에 대입하여 검산
  code = result[0] if len(result)>0 else ''
  code
  ```

  Out[11]:

  ```python
  '167638'
  ```

  In [12]:

  ```python
  review_url = current_url.replace(code, '{}')
  review_url
  ```

  Out[12]:

  ```python
  'https://movie.naver.com/movie/bi/mi/review.nhn?code={}'
  ```

  In [13]:

  ```python
  # 영화 안시성(163533) 리뷰페이지로 바로 이동
  ```

  In [14]:

  ```python
  # 영화제목 검색키 입력
  movie_title = '안시성'
  driver.find_element_by_css_selector('#ipt_tx_srch').send_keys(movie_title)
  ```

  In [15]:

  ```python
  # 검색 클릭
  driver.find_element_by_css_selector('#jSearchArea > div > button').click()
  ```

  In [16]:

  ```python
  # 검색 첫번째 페이지로 이동
  driver.find_element_by_css_selector('#old_content > ul:nth-child(4) > li:nth-child(1) > dl > dt > a').click()
  ```

  In [17]:

  ```python
  # 페이지 BeautifulSoup 객체로 가져온다
  html = driver.page_source
  soup = BeautifulSoup(html, "lxml")
  soup.title
  ```

  Out[17]:

  ```python
  <title>안시성 : 네이버 영화</title>
  ```

  In [18]:

  ```python
  current_url = driver.current_url
  current_url
  ```

  Out[18]:

  ```python
  'https://movie.naver.com/movie/bi/mi/basic.nhn?code=163533'
  ```

  In [19]:

  ```python
  pattern = re.compile("\d{6}")
  result = pattern.findall(current_url)
  code = result[0] if len(result)>0 else ''
  code
  ```

  Out[19]:

  ```python
  '163533'
  ```

  In [20]:

  ```python
  # 영화메인페이지 캡처후 저장
  capture_img = './images/naver_movie_{code}.png'.format(code=code)
  driver.save_screenshot(capture_img)
  Image(capture_img)
  ```

  In [21]:

  ```python
  # 리뷰페이지로 바로 이동
  url_page = review_url.format(code)
  driver.get(url_page)
  ```

  In [22]:

  - 이 이후는 beautiful soup 사용 배웠던 것과 동일하다.

  ```python
  html = driver.page_source
  soup = BeautifulSoup(html, "lxml")
  
  review_cnt = soup.find("span","cnt")
  review_cnt
  ```

  Out[22]:

  ```python
  <span class="cnt">총<em>627</em>건</span>
  ```

  In [23]:

  ```python
  review_cnt2 = review_cnt.find("em").get_text()
  review_cnt2
  ```

  Out[23]:

  ```python
  '627'
  ```

  In [24]:

  ```python
  review_cnt_total = int(review_cnt2.replace(',', ''))
  review_cnt_total
  ```

  Out[24]:

  ```python
  627
  ```

  In [25]:

  ```python
  last_page = review_cnt_total//10 + 1
  last_page
  ```

  Out[25]:

  ```python
  63
  ```

  In [26]:

  ```python
  '네이버영화 "안시성"의 리뷰수는 총 {}건이며, 마지막 페이지는 {} 입니다.'.format(review_cnt_total, last_page)
  ```

  Out[26]:

  ```python
  '네이버영화 "안시성"의 리뷰수는 총 627건이며, 마지막 페이지는 63 입니다.'
  ```

  In [27]:

  ```python
  # 리뷰 마지막 페이지로 이동
  url_page = 'https://movie.naver.com/movie/bi/mi/review.nhn?code={}&page={}'.format(code, last_page)
  driver.get(url_page)
  ```



  #### ※ 셀레니움 웹드라이브를 통해서 소스코드에서 보여지는 내용들은 모두 기존 학습방법으로 크롤링할 수 있습니다.



