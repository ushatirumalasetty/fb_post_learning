from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from django.http import HttpResponse
from fb_post.utils import get_user_posts

from raven.utils import json


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    try:
        posts_list = get_user_posts(
        user_id=user.id)
    except:
        return HttpResponse('HOLA!..........')
    posts_list_json =  json.dumps(posts_list)
    response = HttpResponse(posts_list_json, status=200)
    return response