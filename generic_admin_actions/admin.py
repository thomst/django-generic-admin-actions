from django.db import models
from django.contrib import admin
from django.contrib.admin.utils import model_format_dict
from django.contrib import messages
from django.http.response import HttpResponseBase
from django.http import HttpResponseRedirect
from .forms import GenericActionsForm


# This is mainly slightly adjusted django-code. Since the whole implementation
# of generic-admin-actions follows django's admin-actions implementation.
class GenericActionsMixin:
    """
    A Mixin for ModelAdmin classes to add generic admin actions.
    """
    generic_actions = ()
    generic_action_form = GenericActionsForm

    def changelist_view(self, request, extra_context=None):

        # Get generic actions.
        actions = self.get_generic_actions(request)

        # Respond to the generic actions.
        if (
            actions
            and request.method == "POST"
            and "generic_action_index" in request.POST
            and "_save" not in request.POST
        ):
            response = self.response_generic_action(request)
            return response or HttpResponseRedirect(request.get_full_path())

        # Build the generic action form and populate it with available actions.
        if actions:
            action_form = self.generic_action_form(auto_id=None)
            action_form.fields["generic_action"].choices = self.get_generic_action_choices(request)
        else:
            action_form = None

        # Pass the generic action form as extra_context.
        extra_context = extra_context or dict()
        extra_context['generic_action_form'] = action_form
        return super().changelist_view(request, extra_context=extra_context)

    def response_generic_action(self, request):
        """
        Handle a generic admin action. This is called if a request is POSTed to
        the changelist; it returns an HttpResponse if the action was handled,
        and None otherwise.
        """

        # There can be multiple action forms on the page (at the top
        # and bottom of the change list, for example). Get the action
        # whose button was pushed.
        try:
            action_index = int(request.POST.get("generic_action_index", 0))
        except ValueError:
            action_index = 0

        # Construct the action form.
        data = request.POST.copy()

        # Use the action whose button was pushed
        try:
            data.update({"generic_action": data.getlist("generic_action")[action_index]})
        except IndexError:
            # If we didn't get an action from the chosen form that's invalid
            # POST data, so by deleting action it'll fail the validation check
            # below. So no need to do anything here
            pass

        action_form = self.generic_action_form(data, auto_id=None)
        action_form.fields["generic_action"].choices = self.get_generic_action_choices(request)

        # If the form's valid we can handle the action.
        if action_form.is_valid():
            action = action_form.cleaned_data["generic_action"]
            func = self.get_generic_actions(request)[action][0]
            response = func(self, request)

            # Actions may return an HttpResponse-like object, which will be
            # used as the response from the POST. If not, we'll be a good
            # little HTTP citizen and redirect back to the changelist page.
            if isinstance(response, HttpResponseBase):
                return response
            else:
                return HttpResponseRedirect(request.get_full_path())
        else:
            msg = _("No generic action selected.")
            self.message_user(request, msg, messages.WARNING)
            return None

    def _get_base_generic_actions(self):
        """Return the list of actions, prior to any request-based filtering."""
        actions = []
        actions = (self.get_action(action) for action in self.generic_actions or [])
        # get_action might have returned None, so filter any of those out.
        actions = [action for action in actions if action]

        return actions

    def get_generic_actions(self, request):
        """
        Return a dictionary mapping the names of all generic actions for this
        ModelAdmin to a tuple of (callable, name, description) for each action.
        """
        # If self.generic_actions is set to None that means actions are disabled
        # on this page.
        if self.generic_actions is None:
            return {}
        actions = self._filter_actions_by_permissions(request, self._get_base_generic_actions())
        return {name: (func, name, desc) for func, name, desc in actions}

    def get_generic_action_choices(self, request, default_choices=models.BLANK_CHOICE_DASH):
        """
        Return a list of choices for use in a form object.  Each choice is a
        tuple (name, description).
        """
        choices = [] + default_choices
        for func, name, description in self.get_generic_actions(request).values():
            choice = (name, description % model_format_dict(self.opts))
            choices.append(choice)
        return choices
