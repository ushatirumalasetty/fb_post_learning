import pytest

from django_swagger_utils.drf_server.exceptions import NotFound

from fb_post_v2.presenters.presenter_implementation import \
    PresenterImplementation

from fb_post_v2.constants.exception_messages import INVALID_COMMENT_ID


def test_raise_invalid_comment_id_exception_with_invalid_comment_id():

    # Arrange
    exception_message = INVALID_COMMENT_ID[0]
    exception_res_status = INVALID_COMMENT_ID[1]
    json_presenter = PresenterImplementation()

    # Act
    with pytest.raises(NotFound) as exception:
        json_presenter.raise_invalid_comment_id_exception()

    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status

    
