#!/usr/bin/env python

import os
from setuptools import setup
from pathlib import Path


def read(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, encoding="utf-8") as file:
        return file.read()


def version():
    namespace = {}
    path = Path("generic_admin_actions", "__version__.py")
    exec(path.read_text(), namespace)
    return namespace["__version__"]


version = version()
if 'dev' in version:
    dev_status = 'Development Status :: 3 - Alpha'
elif 'beta' in version:
    dev_status = 'Development Status :: 4 - Beta'
else:
    dev_status = 'Development Status :: 5 - Production/Stable'


setup(
    name="django-generic-admin-actions",
    version=version,
    description="Use item unspecific admin actions in Django admin's changelist view",
    long_description=read("README.rst"),
    long_description_content_type="text/x-rst",
    author="Thomas Leichtfuß",
    author_email="thomas.leichtfuss@posteo.de",
    url="https://github.com/thomst/django-generic-admin-actions",
    license="BSD License",
    platforms=["OS Independent"],
    packages=['generic_admin_actions', 'generic_admin_actions.templatetags'],
    package_data={'generic_admin_actions': ['templates/**'],},
    include_package_data=False,
    install_requires=[
        "Django>=2.2",
    ],
    classifiers=[
        dev_status,
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Framework :: Django :: 5.1",
        "Framework :: Django :: 5.2",
        "Framework :: Django :: 6.0",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
)
