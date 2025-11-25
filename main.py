import feedparser
from transformers import pipeline

# Haber kaynakları (RSS linkleri)
RSS_FEEDS = [
    "https://www.trthaber.com/rss/sondakika.rss",
    "https://www.cnnturk.com/feed/rss/all/news",
    "https://www.hurriyet.com.tr/rss/gundem",
]

# Özetleyici model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def get_news():
    all_news = []

    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:  # her kaynaktan 5 haber
            news = {
                "baslik": entry.title,
                "link": entry.link,
                "aciklama": entry.get("summary", "")
            }
            all_news.append(news)

    return all_news


def summarize_text(text):
    if len(text) < 50:
        return text
    summary = summarizer(text, max_length=70, min_length=30, do_sample=False)
    return summary[0]['summary_text']


def main():
    print("🔍 Haberler toplanıyor...\n")
    news_list = get_news()

    for i, haber in enumerate(news_list, 1):
        print(f"{i}. {haber['baslik']}")
        print("Özet:", summarize_text(haber["aciklama"]))
        print("Link:", haber["link"])
        print("-" * 60)


if __name__ == "__main__":
    main()
