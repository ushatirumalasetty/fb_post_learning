import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_v2.interactors.reply_to_comment_interactor import \
    ReplyToCommentInteractor

from fb_post_v2.presenters import PresenterImplementation
from fb_post_v2.storages import StorageImplementation
from .validator_class import ValidatorClass



@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    comment_id = kwargs["comment_id"]
    request_data = kwargs["request_data"]
    reply_content = request_data["content"]
    user_id = user.id

    comment_storage = StorageImplementation()
    presenter = PresenterImplementation()

    interactor = ReplyToCommentInteractor(comment_storage=comment_storage,
                                          presenter=presenter)

    comment_id_dict = interactor.reply_to_comment(
            user_id=user_id,
            comment_id=comment_id,
            reply_content=reply_content)

    response_data = json.dumps(comment_id_dict)

    return HttpResponse(response_data, status=201)
