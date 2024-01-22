from django.test import TestCase
import random
from .models  import News 
# Create your tests here.

class NewsModelTest(TestCase):
    def news_create(self, 
                     category = 'Sample Category',     title = 'Sample Title',     description = 'Sample Info',     author = 'Sample Author',      heshtag = 'Sample Heshtag'
                ):
        return News.objects.create(
            category=category, title=title, description=description, author=author, heshtag=heshtag
        )
    def test_create_news(self):
        news = self.news_create()
        self.assertTrue(isinstance(news, News))
        self.assertEqual(news.__str__(), news.title)
    
    def test_big_create_news(self):
        num_news = 10000000
        news = [
            News(
                category = f"News {news}",
                title = f"News {news}",
                description = f"description {news}",
                author = f"author {news}",
                heshtag = f"heshtag {news}"
            )
            for news in range(num_news)
        ]
        News.objects.bulk_create(news)
        self.assertEqual(News.objects.count(), num_news)
        
# class NewsModelTest(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         News.objects.create(
#             category = 'Sample Category',
#             title = 'Sample Title',
#             description = 'Sample Info',
#             author = 'Sample Author',
#             heshtag = 'Sample Heshtag'
#         )
    
#     def test_news_category(self):
#         news = News.objects.get(id=10)
#         category = news.category
#         self.assertEqual(category, 'Sample Category')
    
#     def test_news_title(self):
#         news = News.objects.get(id=10)
#         title = news.title
#         self.assertEqual(title, 'Sample Title')
        
#     def test_news_description(self):
#         news = News.objects.get(id=10)
#         description = news.description
#         self.assertEqual(description, 'Sample Info')
        
#     def test_news_author(self):
#         news = News.objects.get(id=10)
#         author = news.author
#         self.assertEqual(author, 'Sample Author')
        
#     def test_news_heshtag(self):
#         news = News.objects.get(id=10)
#         heshtag = news.heshtag
#         self.assertEqual(heshtag, 'Sample Heshtag')