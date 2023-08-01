from django.http import HttpResponseRedirect
from django.contrib import messages


def action_one(modeladmin, request):
    messages.info(request, 'Go with action_one!')
action_one.allowed_permissions = ['change']


def action_two(modeladmin, request):
    messages.info(request, 'Go with action_two!')


def action_three(modeladmin, request):
    messages.info(request, 'Go with action_three!')
    return HttpResponseRedirect(request.get_full_path())
