from django import template

register = template.Library()


# Tag of delays fadeIn picture in gallery
@register.filter(name='delays')
@register.tag
def delays(value, different):
    # print('%.2f' % float(value * float(different)))
    return '%.2f' % float(value * float(different))


