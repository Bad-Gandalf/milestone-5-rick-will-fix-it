from django.apps import apps
from django.test import TestCase
from .apps import StatsConfig

class TestStatsConfig(TestCase):
    def test_app(self):
        self.assertEqual("stats", StatsConfig.name)
        self.assertEqual("stats", apps.get_app_config("stats").name)