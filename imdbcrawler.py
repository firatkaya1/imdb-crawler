import requests
from bs4 import BeautifulSoup

def getDataFromImbdb(url, count):
        res_movie = requests.get(url)
        bs_movie = BeautifulSoup(res_movie.text, "html.parser")
        movies = bs_movie.find_all("div", {"class": "lister-item mode-advanced"})
        count = str(count) + ".json"
        f = open("/home/kaya/imdb/" + str(count), "w")
        f.write("[")
        for movie in movies:
                movie_number = movie.find('h3', {"class": "lister-item-header"}).find_all('span')[0].text
                movie_date = movie.find('h3', {"class": "lister-item-header"}).find_all('span')[1].text.replace("(", "").replace(")", "")
                movie_name = movie.find('img', alt=True)['alt']
                strx = "{\"movie_number\"" + ":" + "\"" + movie_number + "\", \"movie_name\":\"" + movie_name + "\", \"movie_date\":\"" + movie_date + "\"  },"
                f.write(strx + "\n")

        print(count, ". filme kadar kayit edildi")
        f.close()

count = 9750
root = "https://www.imdb.com"
url = "https://www.imdb.com/search/title/?title_type=tv_movie,tv_series,tv_episode,documentary&count=250&start=9750&ref_=adv_nxt"

while True:
        res_movie = requests.get(url)
        bs_movie = BeautifulSoup(res_movie.text, "html.parser")
        yeni = bs_movie.find_all('a', {"class": "lister-page-next next-page"})[0].get('href')
        url = root + yeni
        if not url:
                print("döngü kırıldı")
                break
       # getDataFromImbdb(url, count)
        count = count + 250
        print(count," url --> ", url)