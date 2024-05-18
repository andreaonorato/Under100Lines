import requests as rq
from bs4 import BeautifulSoup
import datetime

url = input("Enter Link: ")
if url.startswith("https://") or url.startswith("http://"):
    data = rq.get(url)
else:
    data = rq.get("https://" + url)
soup = BeautifulSoup(data.text, "html.parser")
links = []
for link in soup.find_all("a"):
    links.append(link.get("href"))

# Generate file name based on current date and time
current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"myLinks_{current_time}.txt"

with open(file_name, 'w') as saved:
    for link in links[:10]:
        print(link, file=saved)