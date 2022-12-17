import requests
import bs4
from itertools import zip_longest
import csv
url="https://www.universityguru.com/universities--egypt"
page = requests.get(url)
src=page.content
#print(src)
universities=[]
ranks = []
links = []
soup  =  bs4.BeautifulSoup (src, "html.parser")
University = soup.find_all("h3",{"class":"h5"})
rank = soup.find_all("span",{"class":"h2"})

for i in range(len(University)):
    universities.append(University[i].text.replace("\n", ""))
    ranks.append(rank[i].text)
for link in soup.findAll('a',{"class":"btn btn-outline-success btn-external btn-sm my-1 rounded-0"}):
    links.append(link.get('href'))

#print(links)
file_list = [universities,ranks,links]
exported = zip_longest(*file_list)
with open("E:/python/python project/test.csv","w") as myproject:
    wr = csv.writer(myproject)
    wr.writerow(["University name", "Rank", "University official website"])
    wr.writerows(exported)
