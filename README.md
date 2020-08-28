# imdb-crawler

# Nedir ? 

http://imdb.com/search/title/?title_type=tv_movie,tv_series,tv_episode,documentary&count=250 adresindeki filmleri json formatına çevirip bunları 250'şerlik parçalar haline getiren basit bir crawler.

# Nasıl çalışır ? 

Repository'de bulunan imdbcrawler.py isimli dosyayı kendi bilgisayarınıza indirin. Çalıştırmadan önce bilgisayarınızda requests ve BeautifulSoup'un yüklü olduğundan emin olun.
Tek yapmanız gerek binlerce parçalık oluşucak json dosyasının nereye kayıt etmek istediğinize karar vermek. 9.Satırda ; 
```python
f = open("kendi_dosya_uzantini_ver" + str(count), "w")  
```
kısmında dosyaların nereye kayit edileceğini belirt. Örnek vermek gerekirse; 
Ben dosyaların /home/kaya/imdb/ isimli yere kayit edilmesini istiyorum. O zaman tek yapmam gereken : 
 
 ```python
 f = open("/home/kaya/imdb/" + str(count), "w") 
```
 
 şeklinde yazmak. 
 


