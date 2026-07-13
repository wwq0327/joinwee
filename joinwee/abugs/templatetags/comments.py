from django import template

register = template.Library()


class FakeCommentNode(template.Node):
    def __init__(self, as_varname=None):
        self.as_varname = as_varname

    def render(self, context):
        if self.as_varname:
            context[self.as_varname] = 0
        return ''


@register.tag
def get_comment_count(parser, token):
    bits = token.split_contents()
    if len(bits) >= 4 and bits[-2] == 'as':
        return FakeCommentNode(as_varname=bits[-1])
    return FakeCommentNode()


@register.tag
def get_comment_list(parser, token):
    return FakeCommentNode()


@register.tag
def render_comment_form(parser, token):
    return FakeCommentNode()


@register.simple_tag
def comment_form_target():
    return '#'
