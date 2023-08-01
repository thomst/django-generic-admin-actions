# -*- coding: utf-8 -*-

from django.contrib import admin
from generic_admin_actions.admin import GenericActionsMixin
from .models import ModelOne
from .models import ModelTwo
from .actions import action_one
from .actions import action_two
from .actions import action_three


@admin.register(ModelOne)
class ModelOneAdmin(GenericActionsMixin, admin.ModelAdmin):
    search_fields = ['id']
    generic_actions = [
        action_one,
        action_two,
        action_three,
    ]


@admin.register(ModelTwo)
class ModelTwoAdmin(GenericActionsMixin, admin.ModelAdmin):
    search_fields = ['id']
    generic_actions = None
