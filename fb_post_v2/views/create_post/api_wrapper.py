import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_v2.interactors.create_post_interactor import CreatePostInteractor

from fb_post_v2.presenters import PresenterImplementation
from fb_post_v2.storages import StorageImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    request_data = kwargs["request_data"]
    post_content = request_data["content"]
    user_id = user.id

    post_storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreatePostInteractor(post_storage=post_storage,
                                      presenter=presenter)

    post_id_dict = interactor.create_post(user_id=user_id,
                                          post_content=post_content)

    response_data = json.dumps(post_id_dict)

    return HttpResponse(response_data, status=201)
