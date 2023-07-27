# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.db.utils import IntegrityError
from generic_admin_actions import __version__
from ...models import ModelOne


def create_test_data():
    try:
        User.objects.create_superuser(
            'admin',
            'admin@testapp.org',
            'adminpassword')
    except IntegrityError:
        pass
    try:
        user = User.objects.create_user(
            'anyuser',
            'anyuser@testapp.org',
            'anyuserpassword',
            is_staff=True)
    except IntegrityError:
        pass
    else:
        perms = ['view_modelone']
        for name in perms:
            perm = Permission.objects.get(codename=name)
            user.user_permissions.add(perm)

    for i in range(5):
        one = ModelOne()
        one.save()


class Command(BaseCommand):
    help = 'Administrative actions.'

    def add_arguments(self, parser):
        parser.add_argument(
            '-c', '--create-test-data',
            action='store_true',
            help='Create testdata.')

    def handle(self, *args, **options):
        if options['create_test_data']:
            create_test_data()
