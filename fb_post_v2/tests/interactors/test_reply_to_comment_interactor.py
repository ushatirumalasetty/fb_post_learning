from unittest.mock import create_autospec

import pytest

from django_swagger_utils.drf_server.exceptions import NotFound

from fb_post_v2.interactors.storages import CommentStorageInterface

from fb_post_v2.interactors.presenters import PresenterInterface

from fb_post_v2.interactors.reply_to_comment_interactor import \
    ReplyToCommentInteractor


class TestReplyToCommentInteractor:

    def test_reply_to_comment_interactor_with_valid_comment_id_details(self):

        # Arrange
        user_id = 1
        comment_id = 1
        reply_content = "Love U Dude!....."
        expected_comment_id = 2
        expected_comment_id_dict_mock = {
            "comment_id": expected_comment_id
        }
        comment_storage = create_autospec(CommentStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = ReplyToCommentInteractor(comment_storage=comment_storage,
                                              presenter=presenter)

        comment_storage. \
            return_comment_id_if_is_comment_id_or_return_parent_comment_id. \
                return_value=1
        comment_storage.reply_to_comment.return_value = expected_comment_id
        presenter.get_reply_to_comment_response.return_value = \
            expected_comment_id_dict_mock

        # Act
        new_comment_id_dict = interactor.reply_to_comment(
            user_id=user_id,
            comment_id=comment_id,
            reply_content=reply_content
        )

        # Assert
        assert new_comment_id_dict == expected_comment_id_dict_mock
        comment_storage.reply_to_comment.assert_called_once_with(
            user_id=user_id,
            comment_id=comment_id,
            reply_content=reply_content
        )
        presenter.get_reply_to_comment_response.assert_called_once_with(
             comment_id=expected_comment_id
        )


    def test_reply_to_comment_interactor_with_invalid_comment_id_raise_exception(
        self
    ):

        # Arrange
        user_id = 1
        comment_id = -1
        reply_content = "Love U Dude!....."
        comment_storage = create_autospec(CommentStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = ReplyToCommentInteractor(comment_storage=comment_storage,
                                              presenter=presenter)

        comment_storage.is_valid_comment_id.return_value = False
        presenter.raise_invalid_comment_id_exception.side_effect = NotFound

        # Act
        with pytest.raises(NotFound):
            interactor.reply_to_comment(user_id=user_id,
                                        comment_id=comment_id,
                                        reply_content=reply_content)


    def test_reply_to_comment_interactor_with_valid_reply_id_details(self):

        # Arrange
        user_id = 1
        comment_id = 2
        reply_content = "Love U Dude!....."
        reply_parent_comment_id = 1
        expected_comment_id = 3
        expected_comment_id_dict_mock = {
            "comment_id": expected_comment_id
        }
        comment_storage = create_autospec(CommentStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = ReplyToCommentInteractor(comment_storage=comment_storage,
                                              presenter=presenter)

        comment_storage. \
            return_comment_id_if_is_comment_id_or_return_parent_comment_id.\
                return_value = reply_parent_comment_id
        comment_storage.reply_to_comment.return_value = expected_comment_id
        presenter.get_reply_to_comment_response.return_value = \
            expected_comment_id_dict_mock

        # Act
        new_comment_id_dict = interactor.reply_to_comment(
            user_id=user_id,
            comment_id=comment_id,
            reply_content=reply_content
        )

        # Assert
        assert new_comment_id_dict == expected_comment_id_dict_mock
        comment_storage.reply_to_comment.assert_called_once_with(
            user_id=user_id,
            comment_id=reply_parent_comment_id,
            reply_content=reply_content
        )
        presenter.get_reply_to_comment_response.assert_called_once_with(
             comment_id=expected_comment_id
        )
