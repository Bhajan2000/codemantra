from django import template
from custom_auth.models import *
register = template.Library()

@register.simple_tag
def get_comment(id):
    data = CommentOnBlog.objects.filter(blog_id =id ).all().order_by("-id")
    return data

@register.simple_tag
def get_com_count(id):
    data = CommentOnBlog.objects.filter(blog_id =id ).count()
    return data

@register.simple_tag
def check_like(blog_id,user_id):
    data_c = LikeOnBlog.objects.filter(blog_id =blog_id,user_id = user_id ).count()
    return data_c

@register.simple_tag
def total_c_like(blog_id):
    data_count          = LikeOnBlog.objects.filter(blog_id = blog_id).count()
    return data_count

@register.simple_tag
def post_dateformat(d):
    if d is not None:
        diff = timezone.now() - d
        s = diff.seconds
        if diff.days == 365:
          return '1 year '
        elif diff.days > 365:
          return '{} year'.format(round(diff.days/365))
        if diff.days == 30:
          return '1 month'
        elif diff.days > 30:
          return '{} month'.format(round(diff.days/30))
        elif diff.days == 1:
            return '1 day'
        elif diff.days > 1:
            return '{} d'.format(diff.days)
        elif s <= 1:
            return 'just now'
        elif s < 60:
            return '{} second'.format(s)
        elif s < 120:
            return '1 munite'
        elif s < 3600:
            return '{} munite'.format(round(s/60))
        elif s < 7200:
            return '1 hour'
        else:
            return '{} hour'.format(round(s/3600))
    else:
        return d
