
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from ..admin import ModelOneAdmin
from ..management.commands.testapp import create_test_data


class GenericActionsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_test_data()

    def setUp(self):
        self.admin = User.objects.get(username='admin')
        self.client.force_login(self.admin)
        self.url = reverse('admin:testapp_modelone_changelist')
        self.action_url = f'{self.url}run_generic_action/'

    def test_form(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)
        for action in ModelOneAdmin.generic_actions:
            self.assertIn(action.__name__, resp.content.decode('utf-8'))

    def test_actions(self):
        post_data = dict(generic_action='action_one')
        resp = self.client.post(self.action_url, post_data, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Go with action_one!', resp.content.decode('utf-8'))
