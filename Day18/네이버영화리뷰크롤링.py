from bs4 import BeautifulSoup
from selenium import webdriver
from IPython.display import Image
from urllib.request import urlopen
import re
import time


# 웹드라이브로 크롬브라우즈 띄운다.
class OpenDriverMovieSite():
    driver_path = "../driver/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)
    url_page = 'https://movie.naver.com/movie/point/af/list.nhn'
    movieName = ''
    allReviews = []
    allReviewsIndex = []
    a = 1

    def __init__(self):
        # 클래스를 실행하면 홈페이지로 이동한다.
        self.driver.get(self.url_page)
        time.sleep(1)

    def ReadCSV(self, movie2018):
        movie_name = movie2018['영화명']
        movie_name[1]
        for i in range(0, len(movie2018)):  # CSV 파일의 Rows 갯수를 뒤에 넣어주세여 (1, Rows갯수)
            #             print(self.movieName)
            print(movie_name[i])
            self.movieName = movie_name[i]
            self.BasicOpen()
            self.InputMovieTitle(movie_name[i])

    def BasicOpen(self):
        # 켜진 홈페이지에서 관련영화를 클릭한 후 새로운 창으로 전환하는 것까지
        # 영화명이 지속적으로 바뀔 것이므로 BasicOpen 함수를 활용
        self.driver.find_element_by_xpath('//*[@id="old_content"]/fieldset/form/select').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="old_content"]/fieldset/form/select/option[2]').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="old_content"]/fieldset/form/input[3]').click()
        time.sleep(0.5)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element_by_xpath(
            '//*[@id="page_content"]/div/div/div/div/form/table/tbody/tr/td/input[1]').click()
        time.sleep(0.5)

    def InputMovieTitle(self, movie_title):
        self.driver.find_element_by_css_selector(
            '#page_content > div > div > div > div > form > table > tbody > tr > td > input.input_type_text_1').send_keys(
            movie_title)
        time.sleep(0.5)
        self.driver.find_element_by_xpath(
            '//*[@id="page_content"]/div/div/div/div/form/table/tbody/tr/td/input[2]').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="page_content"]/div/div/div[2]/table/tbody/tr[2]/td/a/img').click()
        time.sleep(0.5)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="old_content"]/fieldset/form/input[4]').click()

        html = urlopen(self.driver.current_url)
        soup = BeautifulSoup(html, "lxml")
        # 코드값 찾아주기
        pattern = re.compile("\d+")
        result = pattern.findall(self.driver.current_url)
        print(result)
        code = result[0] if len(result) > 0 else ''

        # 리뷰의 총개수
        num = soup.find("strong", "c_88 fs_11").get_text()
        num_total = int(num.replace(',', ''))
        last_page = num_total // 10 + 1
        temp = "번호 : {} // 영화명 : {} // code : {} // num_total : {} // last_page : {}".format(self.a, self.movieName,
                                                                                             code, num_total, last_page)
        self.allReviewsIndex.append(temp)
        #         print("번호 : {} // 영화명 : {} // code : {} // num_total : {} // last_page : {}".format(self.a, self.movieName, code, num_total, last_page))
        self.a = self.a + 1

        #         last_page = 1000 if last_page > 1000 else last_page
        last_page = 1000 if last_page > 1000 else last_page

        self.GetReviews(code, num_total, last_page)

    def GetReviews(self, code, num_total, last_page):
        tmp = []
        for i in range(last_page):

            # 각 리뷰 페이지로 이동해서 그 url로 드라이버 창 넘어가고-> 수프화
            url_page = 'https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword={}&target=&page={}'.format(code,
                                                                                                                  i + 1)
            print("\"{}\"의 {} 페이지를 수집하고 있습니다..".format(self.movieName, url_page))
            html = urlopen(url_page)
            soup = BeautifulSoup(html, "lxml")
            # 리뷰들 뽑아줌
            review = soup.find_all("td", "title")
            for i in range(len(review)):
                review[i] = review[i].get_text()
                review[i] = review[i].replace('\n', '')
                review[i] = review[i].replace(self.movieName, '')  # 왜 영화명을 '' 처리하는지 잘 모르겠지만 우선 둠
                review[i] = review[i].replace('\r', '')
                review[i] = review[i].replace('\t', '')
                review[i] = review[i].replace('신고', '')
                tmp.append(review[i])
        self.allReviews.append(tmp)


if __name__ == "__main__":
    opendrivermoviesite = OpenDriverMovieSite()
    movie2018 = pd.read_csv('movie2018_69.csv', sep=',', encoding='euc-kr')
    opendrivermoviesite.ReadCSV(movie2018)