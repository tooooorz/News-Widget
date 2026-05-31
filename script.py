import requests
import json

TOP_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"

ids = requests.get(TOP_URL).json()

articles = []

for story_id in ids[:3]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    item = requests.get(url).json()

    articles.append({
        "title": item.get("title"),
        "url": item.get("url", ""),
        "score": item.get("score")
    })

with open("news.json", "w") as f:
    json.dump(articles, f, indent=2)
