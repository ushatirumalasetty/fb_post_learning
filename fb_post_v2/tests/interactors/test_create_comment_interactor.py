from unittest.mock import create_autospec

from fb_post_v2.interactors.storages import PostStorageInterface
from fb_post_v2.interactors.storages import CommentStorageInterface

from fb_post_v2.interactors.presenters import PresenterInterface

from fb_post_v2.interactors.create_comment_interactor import \
    CreateCommentInteractor

import pytest

from django_swagger_utils.drf_server.exceptions import NotFound


def test_create_comment_with_invalid_post_id_raise_exception():

    # Arrange
    invalid_post_id = -1
    user_id = 1
    comment_content ='New comment'
    post_storage = create_autospec(PostStorageInterface)
    comment_storage = create_autospec(CommentStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateCommentInteractor(post_storage=post_storage,
                                         comment_storage=comment_storage,
                                         presenter=presenter)

    post_storage.is_valid_post_id.return_value = False
    presenter.raise_invalid_post_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_comment(user_id=user_id,
                                  post_id=invalid_post_id,
                                  comment_content=comment_content)


def test_create_comment_with_valid_details():

    # Arrange
    post_id = 1
    user_id = 1
    comment_content ='New comment'
    expected_comment_id = 1
    expected_comment_id_response = {
        "comment_id": expected_comment_id
    }
    post_storage = create_autospec(PostStorageInterface)
    comment_storage = create_autospec(CommentStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateCommentInteractor(post_storage=post_storage,
                                         comment_storage=comment_storage,
                                         presenter=presenter)

    comment_storage.create_comment.return_value = expected_comment_id
    presenter.get_create_comment_response.return_value = \
        expected_comment_id_response

    # Act
    actual_comment_id_dict = interactor.create_comment(
        user_id=user_id,
        post_id=post_id,
        comment_content=comment_content
    )

    # Assert
    assert actual_comment_id_dict == expected_comment_id_response
    comment_storage.create_comment.assert_called_once_with(
        user_id=user_id,
        post_id=post_id,
        comment_content=comment_content
    )
    presenter.get_create_comment_response.assert_called_once_with(
        comment_id=expected_comment_id
    )