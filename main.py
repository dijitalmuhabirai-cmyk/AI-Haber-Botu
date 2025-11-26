import feedparser
import tweepy
import os

# RSS kaynakları
RSS_FEEDS = [
    "https://www.aa.com.tr/tr/rss/gundem",
    "https://www.trthaber.com/xml_mobile.xml"
]

# Twitter API bilgileri (GitHub Secrets'tan gelecek)
API_KEY = os.getenv("TW_API_KEY")
API_SECRET = os.getenv("TW_API_SECRET")
ACCESS_TOKEN = os.getenv("TW_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("TW_ACCESS_SECRET")

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def fetch_and_tweet():
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        if feed.entries:
            latest = feed.entries[0]
            title = latest.title
            link = latest.link
            tweet = f"{title}\n{link}"
            api.update_status(tweet)
            print("Tweet atıldı:", tweet)

if __name__ == "__main__":
    fetch_and_tweet()
from bot import get_latest_news, post_to_x

def main():
    news_list = get_latest_news()
    if not news_list:
        print("No news found.")
        return
    
    for news in news_list:
        post_to_x(news)

if __name__ == "__main__":
    main()
