from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from django.http import HttpResponse
from fb_post.utils import get_reaction_metrics

from raven.utils import json
from fb_post.constants import INVALID_POST

from django_swagger_utils.drf_server.exceptions import BadRequest
from fb_post.validators import InvalidPostException

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    post_id = kwargs['post_id']
    
    try:
        metrics_dict = get_reaction_metrics(post_id=post_id)
    except InvalidPostException:
        raise BadRequest(*INVALID_POST)
        
    metrics_dict_json = json.dumps(metrics_dict)
    response = HttpResponse(metrics_dict_json, status=200)
    return response
