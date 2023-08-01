
from django.test import TestCase
from django.test import Client
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

    def test_form(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)
        for action in ModelOneAdmin.generic_actions:
            self.assertIn(action.__name__, resp.content.decode('utf-8'))

    def test_actions(self):
        post_data = dict()
        post_data['generic_action'] = ['action_one', 'action_two']
        post_data['generic_action_index'] = 0
        resp = self.client.post(self.url, post_data, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Go with action_one!', resp.content.decode('utf-8'))

        post_data = dict()
        post_data['generic_action'] = ['action_one', 'action_two']
        post_data['generic_action_index'] = 1
        resp = self.client.post(self.url, post_data, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Go with action_two!', resp.content.decode('utf-8'))

        # Using an invalid action_index won't just works. Should not happen
        # though.
        post_data = dict()
        post_data['generic_action'] = ['action_one', 'action_two']
        post_data['generic_action_index'] = 'foobar'
        resp = self.client.post(self.url, post_data, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Go with action_one!', resp.content.decode('utf-8'))

        # Action returning HTTPResponse.
        post_data = dict()
        post_data['generic_action'] = ['action_three']
        post_data['generic_action_index'] = 0
        resp = self.client.post(self.url, post_data, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Go with action_three!', resp.content.decode('utf-8'))

    def test_invalid_actions(self):
        # Invalid action_index
        post_data = dict()
        post_data['generic_action'] = ['action_one', 'action_two']
        post_data['generic_action_index'] = 3
        resp = self.client.post(self.url, post_data, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('No generic action selected.', resp.content.decode('utf-8'))
        self.assertNotIn('Go with action_one!', resp.content.decode('utf-8'))
        self.assertNotIn('Go with action_two!', resp.content.decode('utf-8'))

        # Missing generic_action
        post_data = dict()
        post_data['generic_action'] = []
        post_data['generic_action_index'] = 0
        resp = self.client.post(self.url, post_data, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('No generic action selected.', resp.content.decode('utf-8'))
        self.assertNotIn('Go with action_one!', resp.content.decode('utf-8'))
        self.assertNotIn('Go with action_two!', resp.content.decode('utf-8'))

    def test_action_permission(self):
        client = Client()
        client.force_login(User.objects.get(username='anyuser'))
        resp = client.get(self.url)
        self.assertEqual(resp.status_code, 200)
        self.assertNotIn('action_one', resp.content.decode('utf-8'))
        self.assertIn('action_two', resp.content.decode('utf-8'))

    def test_model_admin_without_actions(self):
        url = reverse('admin:testapp_modeltwo_changelist')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertNotIn('generic_action_index', resp.content.decode('utf-8'))
