# -*- coding: utf-8 -*-

from django.db import models


class ModelOne(models.Model):
    class Meta:
        verbose_name = 'ModelOne'


class ModelTwo(models.Model):
    class Meta:
        verbose_name = 'ModelTwo'
