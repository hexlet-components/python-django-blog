from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from django.urls import reverse
from python_django_blog.articles.models import Article
from python_django_blog.utils import get_test_data


class ArticleTest(TestCase):
    fixtures = ['articles.json']

    @classmethod
    def setUpTestData(cls):
        cls.test_data = get_test_data()

    def assertArticle(self, article, article_data):
        self.assertEqual(article.__str__(), article_data['name'])
        self.assertEqual(article.name, article_data['name'])
        self.assertEqual(article.description, article_data['description'])

    def test_index_page(self):
        response = self.client.get(reverse('articles:index'))
        self.assertEqual(response.status_code, 200)

        articles = Article.objects.all()
        self.assertQuerysetEqual(
            response.context['article_list'],
            articles,
            ordered=False,
        )

    def test_create_page(self):
        response = self.client.get(reverse('articles:create'))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        new_article_data = self.test_data['articles']['new']
        response = self.client.post(reverse('articles:create'), new_article_data)

        self.assertRedirects(response, reverse('articles:index'))
        created_article = Article.objects.get(name=new_article_data['name'])
        self.assertArticle(created_article, new_article_data)

    def test_update_page(self):
        exist_article_data = self.test_data['articles']['existing']
        exist_article = Article.objects.get(name=exist_article_data['name'])
        response = self.client.get(reverse('articles:update', args=[exist_article.pk]))

        self.assertEqual(response.status_code, 200)

    def test_update(self):
        exist_article_data = self.test_data['articles']['existing']
        new_article_data = self.test_data['articles']['new']
        exist_article = Article.objects.get(name=exist_article_data['name'])
        response = self.client.post(
            reverse('articles:update', args=[exist_article.pk]),
            new_article_data,
        )

        self.assertRedirects(response, reverse('articles:index'))
        updated_article = Article.objects.get(name=new_article_data['name'])
        self.assertArticle(updated_article, new_article_data)

    def test_delete_page(self):
        exist_article_data = self.test_data['articles']['existing']
        exist_article = Article.objects.get(name=exist_article_data['name'])
        response = self.client.get(reverse('articles:delete', args=[exist_article.pk]))

        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        exist_article_data = self.test_data['articles']['existing']
        exist_article = Article.objects.get(name=exist_article_data['name'])
        response = self.client.post(reverse('articles:delete', args=[exist_article.pk]))

        self.assertRedirects(response, reverse('articles:index'))
        with self.assertRaises(ObjectDoesNotExist):
            Article.objects.get(name=exist_article_data['name'])

    def test_detail_page(self):
        exist_article_data = self.test_data['articles']['existing']
        exist_article = Article.objects.get(name=exist_article_data['name'])
        response = self.client.get(reverse('articles:detail', args=[exist_article.pk]))

        self.assertEqual(response.status_code, 200)
