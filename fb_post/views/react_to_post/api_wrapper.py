from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from django.http import HttpResponse
from fb_post.utils import react_to_post

from raven.utils import json
from fb_post.constants import INVALID_REACTION_TYPE
from fb_post.constants import INVALID_POST

from django_swagger_utils.drf_server.exceptions import BadRequest
from fb_post.validators import InvalidReactionTypeException
from fb_post.validators import InvalidPostException


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    post_id = kwargs['post_id']
    request_data = kwargs['request_data']
    reaction_type =  request_data['reaction_type']
    
    try:
        react_to_post(
            user_id=user.id,
            post_id=post_id,
            reaction_type=reaction_type
        )
    except InvalidReactionTypeException:
        raise BadRequest(*INVALID_REACTION_TYPE)
    except InvalidPostException:
        raise BadRequest(*INVALID_POST)

    return HttpResponse(status=200)