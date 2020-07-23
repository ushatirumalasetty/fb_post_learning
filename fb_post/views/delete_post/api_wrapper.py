from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from django.http import HttpResponse
from fb_post.utils import delete_post

from raven.utils import json
from fb_post.constants import INVALID_POST, USER_CANNOT_DELETE_POST

from django_swagger_utils.drf_server.exceptions import BadRequest
from fb_post.validators import InvalidPostException, UserCannotDeletePostException


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    post_id = kwargs['post_id']
    user = kwargs['user']

    try:
        delete_post(user_id=user.id, post_id=post_id)
    except InvalidPostException:
        raise BadRequest(*INVALID_POST)
    except UserCannotDeletePostException:
        raise BadRequest(*USER_CANNOT_DELETE_POST)

    return HttpResponse(status=200)