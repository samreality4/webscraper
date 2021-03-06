import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, "html.parser")

title = soup.select(".athing")
subtext = soup.select(".subtext")

print(title)

# def create_custom_hn(links, subtext):
#     hn = []
#     for idx, item in enumerate(links):
#         title = links[idx].getText()
#         href = links[idx].get("href", None)
#         vote = subtext[idx].select(".score")
#         if len(vote):
#             points = int(vote[0].getText().replace(" points", ""))
#             hn.append({"title": title, "link": href, "votes": points})
#         print(hn)
#     return hn

# print(create_custom_hn(links, subtext))
