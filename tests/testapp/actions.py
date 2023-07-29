
from django.contrib import messages


def action_one(modeladmin, request):
    messages.info(request, 'Go with action_one!')
action_one.allowed_permissions = ['change']


def action_two(modeladmin, request):
    messages.info(request, 'Go with action_two!')
