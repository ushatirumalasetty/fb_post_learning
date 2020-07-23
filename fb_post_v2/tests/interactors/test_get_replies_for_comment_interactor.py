from unittest.mock import create_autospec

import pytest

from django_swagger_utils.drf_server.exceptions import NotFound

from fb_post_v2.interactors.storages import CommentStorageInterface

from fb_post_v2.interactors.presenters import PresenterInterface

from fb_post_v2.interactors.get_replies_for_comment_interactor import \
    GetRepliesForCommentInteractor



class TestGetRepliesForCommentInteractor:

    def test_get_replies_for_comment_interactor_with_valid_details(
            self,
            comment_replies_dto):

        # Arrange
        comment_id = 1
        expected_replies_dict_list_mock = comment_replies_dto

        comment_storage = create_autospec(CommentStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetRepliesForCommentInteractor(
            comment_storage=comment_storage, presenter=presenter
        )

        comment_storage.get_replies_for_comment_dto.return_value = \
            expected_replies_dict_list_mock
        presenter.get_replies_for_comment_response.return_value = \
            expected_replies_dict_list_mock

        # Act
        actual_replies_dict_list = interactor.get_replies_for_comment(
            comment_id=comment_id
        )

        # Assert
        assert actual_replies_dict_list == expected_replies_dict_list_mock
        comment_storage.get_replies_for_comment_dto.assert_called_once_with(
            comment_id=comment_id
        )
        comment_storage.is_valid_comment_id.assert_called_once_with(
            comment_id=comment_id
        )
        presenter.get_replies_for_comment_response.assert_called_once_with(
             comment_reply_dtos=expected_replies_dict_list_mock
        )

    def test_get_replies_for_comment_with_invalid_comment_id_raise_exception(
            self
    ):

        # Arrange
        invalid_comment_id = -1
        comment_storage = create_autospec(CommentStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetRepliesForCommentInteractor(
            comment_storage=comment_storage, presenter=presenter
        )

        comment_storage.is_valid_comment_id.return_value = False
        presenter.raise_invalid_comment_id_exception.side_effect = NotFound

        # Act
        with pytest.raises(NotFound):
            interactor.get_replies_for_comment(comment_id=invalid_comment_id)
