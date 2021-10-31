from app import app
import urllib.request,json
from .models import news

News = news.News


# Getting api key
api_key = app.config['NEWS_API_KEY']