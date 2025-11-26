import feedparser
import requests
import os
from time import sleep

RSS_FEEDS = [
    "https://www.aa.com.tr/tr/rss/gundem",
    "https://www.trthaber.com/xml_mobile.xml"
]

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

posted = set()

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

while True:
    for feed in RSS_FEEDS:
        rss = feedparser.parse(feed)
        for entry in rss.entries:
            if entry.link not in posted:
                posted.add(entry.link)
                message = f"{entry.title}\n{entry.link}"
                send_message(message)
                sleep(1)
    sleep(60)
