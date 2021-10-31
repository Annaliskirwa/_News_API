import unittest
from models import news
News = news.News

class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(12,"Apple", "AppleInc","Apple releases Iphone","IPhoine was released today","https://Apple.com")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()