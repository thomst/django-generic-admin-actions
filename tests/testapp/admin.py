# -*- coding: utf-8 -*-

from django.contrib import admin
from generic_admin_actions.admin import GenericActionsModelAdmin
from .models import ModelOne
from .actions import action_one
from .actions import action_two


@admin.register(ModelOne)
class ModelOneAdmin(GenericActionsModelAdmin):
    search_fields = ['id']
    generic_actions = [
        action_one,
        action_two,
    ]
