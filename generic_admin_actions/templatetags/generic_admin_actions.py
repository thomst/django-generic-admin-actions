
from django.template import Library
from django.contrib.admin.templatetags.base import InclusionAdminNode


register = Library()


def generic_admin_actions(context):
    """
    Track the number of times the action field has been rendered on the page,
    so we know which value to use.
    """
    context['generic_action_index'] = context.get('generic_action_index', -1) + 1
    return context


@register.tag(name='generic_admin_actions')
def generic_admin_actions_tag(parser, token):
    return InclusionAdminNode(
        parser,
        token,
        func=generic_admin_actions,
        template_name='generic_actions.html'
    )
