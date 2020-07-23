from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from django.http import HttpResponse
from fb_post.utils import react_to_comment

from raven.utils import json
from fb_post.constants import INVALID_REACTION_TYPE
from fb_post.constants import INVALID_COMMENT

from django_swagger_utils.drf_server.exceptions import BadRequest
from fb_post.validators import InvalidReactionTypeException
from fb_post.validators import InvalidCommentException



@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    comment_id = kwargs['comment_id']
    request_data = kwargs['request_data']
    reaction_type =  request_data['reaction_type']
    
    try:
        react_to_comment(
            user_id=user.id,
            comment_id=comment_id,
            reaction_type=reaction_type
        )
    except InvalidReactionTypeException:
        raise BadRequest(*INVALID_REACTION_TYPE)
    except InvalidCommentException:
        raise BadRequest(*INVALID_COMMENT)

    return HttpResponse(status=200)