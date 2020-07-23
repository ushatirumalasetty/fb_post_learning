from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from django.http import HttpResponse
from fb_post.utils import get_total_reaction_count

from raven.utils import json

from django_swagger_utils.drf_server.exceptions import BadRequest

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    count_dict = get_total_reaction_count()
    count_dict_json = json.dumps(count_dict)
    response =  HttpResponse(count_dict_json, status=200)
    return response