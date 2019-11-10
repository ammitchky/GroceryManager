import json

import requests
from bs4 import BeautifulSoup

BASE_URL = "http://www.stilltasty.com/searchitems/index/"
SUBSECTIONS = [26, 28, 25, 6, 9, 31, 27, 30, 7, 5]

all_items = set()

for section in SUBSECTIONS:
    page = 1
    while True:
        r = requests.get(f"{BASE_URL}{section}?page={page}")
        print(f"{BASE_URL}{section}?page={page}")
        if "No Search Item Found." in r.text:
            break
        soup = BeautifulSoup(r.text, "html.parser")
        div = soup.find("div", {"class": "search-list"})
        for link in div.findAll("a"):
            all_items.add(link["href"])
        page += 1

# with open("list.txt", 'w') as f:
#     f.write('\n'.join(all_items))

# print('Saved list')

# with open("list.txt", "r") as f:
#     all_items = f.readlines()

# import os.path
# from os import path

# if path.exists("recent.txt"):
#     with open("recent.txt", "r") as f:
#         start = f.readline().strip()
# else:
#     start = None

# reached_start = False

scraped_items = {}

for item in all_items:
    item = item.strip()
    # if start is not None and not reached_start:
    #     if item == start:
    #         reached_start = True
    #     else:
    #         continue
    r = requests.get(item.replace("https", "http"))
    soup = BeautifulSoup(r.text, "html.parser")
    div = soup.find("div", {"class": "food-storage-container"})
    title = div.findNext("h2")
    title = title.text.strip()
    methods = div.findAll("div", {"class": "food-inside clearfix"})
    scraped_methods = {}
    for method in methods:
        name = method.findNext("div").findNext("span").text
        length = (
            method.findNext("div", {"class": "food-storage-right"})
            .findNext("span")
            .text
        )
        scraped_methods[name] = length.strip()
    scraped_items[title] = scraped_methods
    # with open("recent.txt", "w") as f:
    #     f.write(item)
    # with open(f"data\\{item.split('/')[-1]}.json", "w") as f:
    #     f.write(json.dumps(scraped_item))


with open(f"data", "w") as f:
    f.write(json.dumps(scraped_items))
