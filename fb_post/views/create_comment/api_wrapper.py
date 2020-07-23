from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from fb_post.utils import create_comment

from raven.utils import json
from fb_post.constants import INVALID_COMMENT_CONTENT
from fb_post.constants import INVALID_POST

from django_swagger_utils.drf_server.exceptions import BadRequest
from fb_post.validators import InvalidPostException
from fb_post.validators import InvalidCommentContent



@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    request_data = kwargs['request_data']
    post_id = request_data['post_id']
    comment_content = request_data['content']
    
    try:
        comment_id = create_comment(
            user_id=user.id,
            post_id=post_id,
            comment_content = comment_content
            )
    except InvalidPostException:
        raise BadRequest(*INVALID_POST)
    except InvalidCommentContent:
        raise BadRequest(*INVALID_COMMENT_CONTENT)
    
    json_data = json.dumps({"comment_id": comment_id})
    response = HttpResponse(json_data, status=201)

    return response