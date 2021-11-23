from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_view_homepage(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_index(self):
        response = self.client.get(url_for('noises'))
        self.assertEqual(response.status_code, 200)

    def test_pig_noise(self):
        with requests_mock.Mocker() as m:
            m.get('http://animal_api:5000/get/animal', text='pig')
            m.get('http://animal_api:5000/get/noise', text='oink')

            response = self.client.get(url_for('noises'))
            self.assertEqual(response.status_code, 200)

    def test_cow_noise(self):
        with requests_mock.Mocker() as m:
            m.get('http://animal_api:5000/get/animal', text='cow')
            m.get('http://animal_api:5000/get/noise', text='moo')

            response = self.client.get(url_for('noises'))
            self.assertEqual(response.status_code, 200)

    def test_dog_noise(self):
        with requests_mock.Mocker() as m:
            m.get('http://animal_api:5000/get/animal', text='dog')
            m.get('http://animal_api:5000/get/noise', text='woof')

            response = self.client.get(url_for('noises'))
            self.assertEqual(response.status_code, 200)