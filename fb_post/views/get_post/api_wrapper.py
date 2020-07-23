from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from fb_post.utils import get_post

from raven.utils import json
from fb_post.constants import INVALID_POST

from django_swagger_utils.drf_server.exceptions import BadRequest
from fb_post.validators import InvalidPostException


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    post_id = kwargs['post_id']
    
    try:
        post_details_dict = get_post(post_id=post_id)
    except InvalidPostException:
        raise BadRequest(*INVALID_POST)

    post_details_json = json.dumps(post_details_dict)
    response = HttpResponse(post_details_json, status=200)
    
    return response
