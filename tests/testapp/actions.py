
from django.contrib import messages
from django.contrib import admin


@admin.action(permissions=['change'])
def action_one(modeladmin, request):
    messages.info(request, 'Go with action_one!')


@admin.action(description='Run action two.')
def action_two(modeladmin, request):
    messages.info(request, 'Go with action_two!')
