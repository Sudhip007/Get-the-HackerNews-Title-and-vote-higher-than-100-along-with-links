import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/news")
res2 = requests.get("https://news.ycombinator.com/news?p2")
#print(res.text)
soup = BeautifulSoup(res.text,'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
#print(soup.body.contents)

links = soup.select('.storylink')
links2 = soup2.select('.storylink')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')
#print(links)

mega_link = links + links2
mega_subtext = subtext + subtext2

def sorted_by_votes(hnlist):
    return sorted(hnlist,key= lambda k:k['vote'],reverse=True)

def create_custom_hn(links,subtext):
    hn=[]
    for  idx,item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points>99:
                hn.append({'title':title, 'href':href, 'vote': points})
    return sorted_by_votes(hn)

pprint.pprint(create_custom_hn(mega_link,mega_subtext))