from django.apps import apps
from django.test import TestCase
from .apps import BlogConfig

class BlogConfigConfig(TestCase):
    def test_app(self):
        self.assertEqual("blog",BlogConfig.name)
        self.assertEqual("blog", apps.get_app_config("blog").name)