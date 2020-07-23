from unittest.mock import create_autospec

import pytest

from django_swagger_utils.drf_server.exceptions import NotFound

from fb_post_v2.interactors.storages import PostStorageInterface

from fb_post_v2.interactors.presenters import PresenterInterface

from fb_post_v2.interactors.delete_post_interactor import \
    DeletePostInteractor

from fb_post_v2.exceptions import UserCannotDeleteException


class TestDeletePostInteractor:

    def test_delete_post_interactor_interactor_with_valid_details(self):

        # Arrange
        user_id = 1
        post_id = 1
        post_storage = create_autospec(PostStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor =DeletePostInteractor(post_storage=post_storage,
                                         presenter=presenter)

        # Act
        interactor.delete_post(user_id=user_id, post_id=post_id)
    
        # Assert
        post_storage.is_valid_post_id.assert_called_once_with(post_id=post_id)
        post_storage.delete_post.assert_called_once_with(post_id=post_id)


    def test_delete_post_interactor_with_invalid_post_id_raise_exception(
        self
    ):

        # Arrange
        user_id = 1
        invalid_post_id = -1
        post_storage = create_autospec(PostStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor =DeletePostInteractor(post_storage=post_storage,
                                         presenter=presenter)

        post_storage.is_valid_post_id.return_value = False
        presenter.raise_invalid_post_id_exception.side_effect = NotFound

        # Act
        with pytest.raises(NotFound):
            interactor.delete_post(user_id=user_id, post_id=invalid_post_id)


    def test_delete_post_interactor_with_invalid_user_id_to_delete_post_raise_exception(
        self
    ):

        # Arrange
        user_id = 2
        post_id = 1
        post_storage = create_autospec(PostStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor =DeletePostInteractor(post_storage=post_storage,
                                         presenter=presenter)

        post_storage.is_post_created_by_user.return_value = False
        presenter.raise_user_cannot_delete_exception.side_effect = \
            UserCannotDeleteException #TodDo -done change the exception

        # Act
        with pytest.raises(UserCannotDeleteException):
            interactor.delete_post(user_id=user_id, post_id=post_id)
            #TODO need to use custome exceptions

