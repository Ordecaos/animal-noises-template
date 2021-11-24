import unittest
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestName(TestBase):
    def test_view(self):
        response = self.clent.get(url_for("/animal/name"))
        self.assertEqual(response.status_code, 200)

class TestNoise(TestBase):
    def test_pig(self):
        response = self.clent.post(url_for("/animal/noise"), data="Pig")
        self.assertIn(b'Oink', response.data)

    def test_cow(self):
        response = self.clent.post(url_for("/animal/noise"), data="Cow")
        self.assertIn(b'Moo', response.data)

    def test_dog(self):
        response = self.clent.post(url_for("/animal/noise"), data="Dog")
        self.assertIn(b'Woof', response.data)

    def test_other(self):
        response = self.clent.post(url_for("/animal/noise"), data="Duck")
        self.assertIn(b'There is no noise for that', response.data)