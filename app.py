
from flask import Flask, render_template
from newsapi.newsapi_client import NewsApiClient

app = Flask(__name__)


@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key='08643f54add84e678202dedfaf6f04f9')
    topheadlines = newsapi.get_top_headlines(sources='the-times-of-india')
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist = zip(news, desc, img)
    return render_template('index.html', context=mylist)


@app.route('/bbc/')
def bbc():
    newsapi = NewsApiClient(api_key='08643f54add84e678202dedfaf6f04f9')
    topheadlines = newsapi.get_top_headlines(sources='techcrunch')
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist = zip(news, desc, img)
    return render_template('bbc.html', context=mylist)


if __name__ == '__main__':
    app.run(debug=True)