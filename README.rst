=======================================
Welcome to django-generic-admin-actions
=======================================

.. image:: https://github.com/thomst/django-generic-admin-actions/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/thomst/django-generic-admin-actions/actions/workflows/ci.yml
   :alt: Run tests for django-generic-admin-actions

.. image:: https://coveralls.io/repos/github/thomst/django-generic-admin-actions/badge.svg?branch=main
   :target: https://coveralls.io/github/thomst/django-generic-admin-actions?branch=main
   :alt: coveralls badge

.. image:: https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue
   :target: https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue
   :alt: python: 3.7, 3.8, 3.9,3.9,3.10

.. image:: https://img.shields.io/badge/django-2.2%20%7C%203.0%20%7C%203.1%20%7C%203.2%20%7C%204.0%20%7C%204.1%20%7C%204.2-orange
   :target: https://img.shields.io/badge/django-2.2%20%7C%203.0%20%7C%203.1%20%7C%203.2%20%7C%204.0%20%7C%204.1%20%7C%204.2-orange
   :alt: django: 2.2, 3.0, 3.1, 3.2, 4.0, 4.1, 4.2


Description
===========
Django-generic-admin-actions are admin actions without an item selection. They
work exactly like original admin actions but without taking a queryset. This is
useful for actions that are model (and not object) related or that should
manipulate model objects as a whole.


Installation
============
Install from pypi.org::

    pip install django-generic-admin-actions


Getting started
===============
Add generic_admin_actions to your installed apps::

    INSTALLED_APPS = [
        'generic_admin_actions',
        'django.contrib.admin',
        ...
    ]

Since we overwrite the change_list.html template the app must be listed before
django's admin-site.

Use the GenericActionsMixin for your ModelAdmin classes and add some actions::

    from django.contrib import admin
    from generic_admin_actions import GenericActionsMixin

    def my_action(modeladmin, request):
        # Do some stuff here.

    class MyModelAdmin(GenericActionsMixin, admin.ModelAdmin):
        ...
        generic_actions = [
            my_action,
            ...
        ]

Generic admin actions working all the same as original admin actions with the
difference that their don't take a queryset. So for more advanced setups like
actions with intermediate pages please follow django's official documentation.


Usage
=====
On your model's change-list-view choose the generic action from the dropdown and
press the "Go" button.