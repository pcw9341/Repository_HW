import requests
from bs4 import BeautifulSoup
from note_book import extract_info
import csv

file=open("movie.csv",mode="w",newline="")
writer=csv.writer(file)
writer.writerow(["image","title","star","director","actor","date"])

Movie_URL = "https://movie.naver.com/movie/running/current.nhn"
Movie_html = requests.get(Movie_URL)
Movie_soup = BeautifulSoup(Movie_html.text,"html.parser")

Movie_list_box = Movie_soup.find("ul",{"class":"lst_detail_t1"})
Movie_list = Movie_list_box.find_all("li")

final_result = []
for movie in Movie_list:
  image = movie.find("div",{"class":"thumb"}).find("img").get("src")
  title = movie.find("dl",{"class":"lst_dsc"}).find("dt",{"class":"tit"}).find("a").text
  star = movie.find("dl",{"class":"lst_dsc"}).find("dd",{"class":"star"}).find("span",{"class":"num"}).text
  director = movie.find("dl",{"class":"lst_dsc"}).find("span",{"class":"link_txt"}).find("a").text
  dd_list = movie.find("dl",{"class":"lst_dsc"}).find("dl",{"class":"info_txt1"}).find_all("dd")
  if len(dd_list) < 3:
      actor = "배우정보없음"
  else:
      actor = movie.find("dl",{"class":"lst_dsc"}).find("dl",{"class":"info_txt1"}).find_all("dd")[2].get_text(strip=True)
  date = movie.find("dl",{"class":"lst_dsc"}).find("dl",{"class":"info_txt1"}).find_all("dd")[0].get_text(strip=True)[-13:-3]
  movie_info = {
      "image":image,
      "title":title,
      "star":star,
      "director":director,
      "actor":actor,
      "date":date
  }
  final_result.append(movie_info)

for result in final_result:
    print(result)
    row = []
    row.append(result["image"])
    row.append(result["title"])
    row.append(result["star"])
    row.append(result["director"])
    row.append(result["actor"])
    row.append(result["date"])
    writer.writerow(row)
print(final_result)

