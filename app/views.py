from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news = "News API"
    return render_template('index.html', news=news)

@app.route('/news/<news_id>')
def news(news_id):

    '''
    View news page function that returns the news article
    '''
    return render_template('news.html',id = news_id)