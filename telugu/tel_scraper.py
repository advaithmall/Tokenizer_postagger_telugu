import requests
from bs4 import BeautifulSoup
import pprint
import urllib.parse


url = 'https://www.teluguone.com/grandalayam/mobile/'
#base_url = "https://allnovel.net"
req = requests.get(url)
html_content = req.content
soup = BeautifulSoup(html_content, 'html5lib')
#print(soup)
my_list = []    
news_corpus = soup.select('p > a')
for i in news_corpus:
    link = i.get('href')
    print(link)
    if link not in my_list:
        my_list.append(link)
pprint.pprint(my_list)
max_p=900
p=0
corpus=""
for my_url in my_list:
    print("Following", my_url)
    my_req = requests.get(my_url)
    my_html = my_req.content
    my_soup = BeautifulSoup(my_html,'html5lib')
    my_corpus = my_soup.select("p")
    for l in my_corpus:
        with open("telcorpus.txt", "a") as file:
            file.write(l.get_text())
        p+=1
        print(">>>",p)
        if (p>=max_p):
            break
    if (p>=max_p):
        break
        #print(l.get_text())
    temp = my_soup.select("#select_main > span > a")
    if temp:
        if len(temp)==1:
            temp_link = temp[0].get("href")
        else:
            temp_link = temp[-1].get("href")
        if temp_link not in my_list:
            my_list.append(temp_link)

    
# print(corpus)
# with open("telcorpus.txt", "w") as file:
#     print(corpus, file=file)








