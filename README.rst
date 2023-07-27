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
Django-generic-admin-actions provides an easy way to add an action form to a
change-list to run generic actions for a specific model independently from the
item selection.


Installation
============
Install from pypi.org::

    pip install django-generic-admin-actions

Setup
=====

Add generic_admin_actions to your installed apps::

    INSTALLED_APPS = [
        'generic_admin_actions',
        ...
    ]

Use the GenericActionsModelAdmin class and add a generic action::

    from generic_admin_actions import GenericActionsModelAdmin

    def my_action(modeladmin, request):
        # Do some stuff here.

    class MyModelAdmin(GenericActionsModelAdmin):
        ...
        generic_actions = [
            my_action,
            ...
        ]

Setup with an intermediate page
===============================

TODO


Usage
=====

On your model's change-list-view choose the generic action from the dropdown and
press the "Go" button.