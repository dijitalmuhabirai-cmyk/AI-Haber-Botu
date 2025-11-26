import os
import requests
import feedparser

BEARER_TOKEN = os.environ["BEARER_TOKEN"]

RSS_FEEDS = [
    "https://www.aa.com.tr/tr/rss/gundem",
    "https://www.trthaber.com/xml_mobile.xml"
]

def get_latest_news():
    news_list = []
    for feed in RSS_FEEDS:
        parsed = feedparser.parse(feed)
        if parsed.entries:
            entry = parsed.entries[0]
            title = entry.title
            link = entry.link
            news_list.append(f"{title}\n{link}")
    return news_list

def post_to_x(text):
    url = "https://api.twitter.com/2/tweets"
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {"text": text}
    requests.post(url, headers=headers, json=payload)

if __name__ == "__main__":
    news = get_latest_news()
    for item in news:
        post_to_x(item)
