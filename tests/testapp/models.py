# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _


class ModelOne(models.Model):
    pass

    class Meta:
        verbose_name = _('ModelOne')
