from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from django.http import HttpResponse
from fb_post.utils import reply_to_comment

from raven.utils import json
from fb_post.constants import INVALID_COMMENT
from fb_post.constants import INVALID_REPLY_CONTENT

from django_swagger_utils.drf_server.exceptions import BadRequest
from fb_post.validators import InvalidCommentException
from fb_post.validators import InvalidReplyContent

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    comment_id = kwargs['comment_id']
    request_data = kwargs['request_data']
    reply_content = request_data['content']
    
    try:
        reply_id = reply_to_comment(
            user_id=user.id,
            comment_id=comment_id,
            reply_content=reply_content
            )
    except InvalidReplyContent:
        raise BadRequest(*INVALID_REPLY_CONTENT)
    except InvalidCommentException:
        raise BadRequest(*INVALID_COMMENT)
    coment_id_json = json.dumps({"comment_id": reply_id})
    response = HttpResponse(coment_id_json, status=201)
    return response