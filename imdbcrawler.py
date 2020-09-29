import requests
from bs4 import BeautifulSoup

def getDataFromImbdb(url,count):
        res_movie = requests.get(url, headers=headers)
        bs_movie = BeautifulSoup(res_movie.text, "html.parser")
        movies = bs_movie.find_all("div", {"class": "lister-item mode-advanced"})
        count = str(count) + ".json"
        f = open("/home/kaya/imdb/" + str(count), "w")
        f.write("[")
        for movie in movies:
                try:
                        movie_number = movie.find('h3', {"class": "lister-item-header"}).find_all('span')[0].text.replace("\n", "").replace("\t", "").replace(".", "").strip()
                except:
                        movie_number = "NOTFOUND"
                        pass
                try:
                        movie_genre = movie.find('div', {"class": "lister-item-content"}).find_all('p', {"class": "text-muted"})[0].find('span', {"class": "genre"}).text.replace("\n", "").replace("\t", "").strip()
                except:
                        movie_genre ="NOTFOUND"
                        pass

                try:
                        movie_date = movie.find('h3', {"class": "lister-item-header"}).find_all('span')[1].text.replace("(", "").replace(")", "").replace("\n", "").replace("\t", "").strip()
                except:
                        movie_date = "NOTFOUND"
                        pass

                try:
                        movie_sub_info = movie.find('div', {"class": "lister-item-content"}).find_all('p', {"class": "text-muted"})[1].text.replace("\n", "").replace("\t", "").replace("\"","").strip()
                except:
                        movie_sub_info = "NOTFOUND"
                        pass
                try:
                        movie_votes = movie.find('div', {"class": "lister-item-content"}).find_all('p', {"class": "sort-num_votes-visible"})[0].find_all('span')[1].text.replace("\n","").replace("\t", "").strip()
                except:
                        movie_votes = "NOTFOUND"
                        pass
                try:
                        movie_time = movie.find('div', {"class": "lister-item-content"}).find_all('p', {"class": "text-muted"})[0].find('span', {"class": "runtime"}).text
                except:
                        movie_time = "NOTFOUND"
                        pass
                try:
                        movie_stars = movie.find('div', {"class": "lister-item-content"}).find_all('p', {"class": ""})[0].text.replace("\n", "").replace("\t", "").replace("Stars:", "").strip()
                except:
                        movie_stars ="NOTFOUND"
                        pass

                try:
                        movie_img = movie.find('div', {"class": "lister-item-image"}).find('img').get('loadlate')
                except:
                        movie_img = "NOTFOUND"
                        pass
                try:
                        movie_name = movie.find('div', {"class": "lister-item-content"}).find('h3').find('a').text
                except:
                        movie_name = "NOTFOUND"
                        pass

                try:
                        movie_rating = movie.find('div', {"class": "inline-block ratings-imdb-rating"}).text.replace("\n", "").strip()

                except:
                        movie_rating = "NOTFOUND"
                        pass


                json = "{\"movie_number\":\"" + str(movie_number.strip()) + "\", \"movie_name\":\"" + str(movie_name) + "\", \"movie_vote\":\"" + str(movie_votes.replace(",","")) + "\", \"movie_date\":\"" + str(movie_date) + "\", \"movie_rating\":\"" + str(movie_rating) + "\", \"movie_time\":\"" + str(movie_time) + "\", \"movie_genre\":\"" + str(movie_genre) + "\", \"movie_stars\":\"" + str(movie_stars) + "\", \"movie_subInfo\":\"" + str(movie_sub_info) + "\", \"movie_img\":\"" + str(movie_img) + "\"},"
                f.write(json + "\n")

        f.write("]")
        f.close()

count = 0
headers = {'User-Agent': 'Mozilla/5.0 (Macintossh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

root = "https://www.imdb.com"
url = "https://www.imdb.com/search/title/?title_type=feature,tv_movie,tv_special,documentary,short,video&user_rating=3.0,&num_votes=100,&sort=num_votes,desc&count=250"

while True:
        getDataFromImbdb(url, count)
        res_movie = requests.get(url, headers=headers)
        bs_movie = BeautifulSoup(res_movie.text, "html.parser")
        yeni = bs_movie.find_all('a', {"class": "lister-page-next next-page"})[0].get('href')
        url = root + yeni
        count = count + 250
        print(count, " tamamlandı.")

