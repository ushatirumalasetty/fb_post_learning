from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from django.http import HttpResponse
from fb_post.utils import get_user_posts

from raven.utils import json


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    offset = kwargs['request_query_params']['offset']
    limit = kwargs['request_query_params']['limit']
    user = kwargs['user']
    user_posts_details_dict = get_user_posts(
        user_id=user.id,
        offset=offset,
        limit=limit
        )
    user_posts_details_dict_json =  json.dumps(user_posts_details_dict)
    response = HttpResponse(user_posts_details_dict_json, status=200)
    return response