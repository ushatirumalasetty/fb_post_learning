from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from raven.utils import json
from django.http import HttpResponse
from fb_post.utils import get_posts_with_more_positive_reactions


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    post_ids_list = get_posts_with_more_positive_reactions()
    post_ids_list_json = json.dumps(post_ids_list)
    response = HttpResponse(post_ids_list_json, status=200)
    return response
