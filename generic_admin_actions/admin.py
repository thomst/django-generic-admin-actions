from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path
from django import forms
from .forms import GenericActionsForm


class GenericActionsModelAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change-list.html'
    generic_actions = list()

    def get_urls(self):
        urls = super().get_urls()
        urls.insert(0, path('run_generic_action/', self.run_generic_action))
        return urls

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or dict()

        if self.generic_actions:
            # Build choices for the generic actions form.
            actions = self.get_generic_actions()
            choices = [(k, k.replace('_', ' ')) for k in actions]
            choices.insert(0, ('', '---------'))

            # Build generic actions form.
            form = GenericActionsForm()
            form.fields['generic_action'].widget = forms.Select(choices=choices)

            # Add form to extra_context.
            extra_context['generic_actions_form'] = form

        return super().changelist_view(request, extra_context=extra_context)

    def get_generic_actions(self):
        actions = dict()
        for action in self.generic_actions:
            name = getattr(action, '__name__', repr(action))
            actions[name] = action
        return actions

    def run_generic_action(self, request):
        action = request.POST.get('generic_action', None)
        actions = self.get_generic_actions()
        actions[action](self, request)
        return HttpResponseRedirect('../')
