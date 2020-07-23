from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from django.http import HttpResponse
from fb_post.utils import get_replies_for_comment

from raven.utils import json
from fb_post.constants import INVALID_COMMENT

from django_swagger_utils.drf_server.exceptions import BadRequest
from fb_post.validators import InvalidCommentException

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    comment_id = kwargs['comment_id']
    
    try:
        replies_details_list = get_replies_for_comment(
            comment_id=comment_id
            )
    except InvalidCommentException:
        raise BadRequest(*INVALID_COMMENT)
    replies_details_list_json = json.dumps(replies_details_list)
    response = HttpResponse(replies_details_list_json, status=200)
    return response