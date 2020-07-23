import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_v2.interactors.create_comment_interactor import \
    CreateCommentInteractor

from fb_post_v2.presenters import PresenterImplementation
from fb_post_v2.storages import StorageImplementation
from .validator_class import ValidatorClass



@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    request_data = kwargs["request_data"]
    comment_content = request_data["content"]
    post_id = request_data['post_id']
    user_id = user.id

    post_storage = StorageImplementation()
    comment_storage = StorageImplementation()
    presenter = PresenterImplementation()

    interactor = CreateCommentInteractor(post_storage=post_storage,
                                         comment_storage=comment_storage,
                                         presenter=presenter)

    comment_id_dict = interactor.create_comment(
        user_id=user_id,
        post_id=post_id,
        comment_content=comment_content)

    response_data = json.dumps(comment_id_dict)

    return HttpResponse(response_data, status=201)
