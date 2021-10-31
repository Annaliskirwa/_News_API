from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    sources = get_news('sources')
    news = "News API"
    return render_template('index.html', news=news, sources=sources)

@app.route('/news/<news_id>')
def news(news_id):

    '''
    View news page function that returns the news article
    '''
    return render_template('news.html',id = news_id)