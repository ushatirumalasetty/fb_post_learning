
from unittest.mock import create_autospec
from fb_post_v2.interactors.storages.storage_interface import \
    StorageInterface

from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface

from fb_post_v2.interactors.create_comment_interface import CreateCommentInteractor
from fb_post_v2.interactors.reply_to_comment_interactor import ReplyToCommentInteractor

from e
import pytest
from django_swagger_utils.drf_server.exceptions import NotFound


def test_with_invalid_post_id_raise_exception():
    # Arrange
    invalid_post_id = -1
    user_id = 1
    comment_content ='New comment'
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.is_valid_post_id.return_value = False
    
    interactor = CreateCommentInteractor(
        storage=storage,
        presenter=presenter
        )
    presenter.raise_invalid_post_id_exception.side_effect = NotFound
    # Act
    with pytest.raises(NotFound):
        interactor.create_comment(
            user_id=user_id,
            post_id=invalid_post_id,
            comment_content=comment_content
            )


def test_reply_to_comment_with_invalid_comment_id_raise_exception():
    
    # Arrange
    user_id=1
    invalid_comment_id = -1
    reply_content='Replyt Content'

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = ReplyToCommentInteractor(
        storage=storage
        presenter=presenter
        )
    so
    # Act
    interactor.reply_to_comment(
        user_id=user_id,
        comment_id=invalid_comment_id,
        reply_content=reply_content
        )
    # Assert