# from selenium import webdriver

# import chromedriver_autoinstaller

# path = chromedriver_autoinstaller.install()
# driver = webdriver.Chrome(path)

# driver.get('https://movie.daum.net/moviedb/grade?movieId=147615')

# print(driver.page_source)
import requests

url = "https://comment.daum.net/apis/v1/posts/147615/comments"

r = requests.get(url)
print(r.text)






