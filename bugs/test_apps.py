from django.apps import apps
from django.test import TestCase
from .apps import BugsConfig

class TestBugsConfig(TestCase):
    def test_app(self):
        self.assertEqual("bugs",BugsConfig.name)
        self.assertEqual("bugs", apps.get_app_config("bugs").name)