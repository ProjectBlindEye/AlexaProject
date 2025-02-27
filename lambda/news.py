import requests
import datetime

URL = "https://www.insignia.vc/startup_info/data.json"

def get_data():
    response = requests.get(URL)
    response_json = response.json()
    return response_json

def get_insignia_news():
    response_json = get_data()

    companies = response_json["portfolios"]
    articles = []
    for company in companies:
        articles.append(
            {
                "title": company["public_info"]["external_article_title"],
                "source": company["public_info"]["external_article_source"],
                "url": company["public_info"]["external_article_link"],
                "date": company["public_info"]["external_article_date"],
            }
        )

    articles.sort(
        key=lambda article: datetime.datetime.strptime(article["date"] or "1970-01-01", "%Y-%m-%d"),
        reverse=True
    )

    return articles

def get_other_news():
    response_json = get_data()

    data = response_json["latest_articles"]
    articles = []
    for article in data:
        articles.append(
            {
                "title": article["title"],
                "image": article["image"],
                "date": article["date"],
            }
        )

    articles.sort(
        key=lambda article: datetime.datetime.strptime(article["date"] or "1970-01-01T00:00:00", "%Y-%m-%dT%H:%M:%S"),
        reverse=True
    )

    return articles
