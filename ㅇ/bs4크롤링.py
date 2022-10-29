import requests
from bs4 import BeautifulSoup

#reqeusts 라이브러리 이용 가져오기
htmls = requests.get('https://movie.daum.net/moviedb/grade?movieId=147615')

print(htmls.text)