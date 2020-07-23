from unittest.mock import create_autospec

import pytest

from django_swagger_utils.drf_server.exceptions import NotFound

from fb_post_v2.interactors.storages import PostStorageInterface
from fb_post_v2.interactors.storages import ReactionStorageInterface

from fb_post_v2.interactors.presenters import PresenterInterface
from fb_post_v2.interactors.react_to_post_interactor import \
    ReactToPostInteractor

from fb_post_v2.constants import ReactionTypeEnum

from fb_post_v2.exceptions import ReactionDoesNotExists


class TestReactToPostInteractor:

    def test_react_to_post_interactor_with_first_time_react_to_post(self):

        # Arrange
        user_id = 1
        post_id = 1
        reaction_type = ReactionTypeEnum.WOW.value

        post_storage = create_autospec(PostStorageInterface)
        reaction_storage = create_autospec(ReactionStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = ReactToPostInteractor(post_storage=post_storage,
                                           reaction_storage=reaction_storage,
                                           presenter=presenter)

        reaction_storage.validate_post_reaction_if_exists_get_reaction_type. \
            side_effect = ReactionDoesNotExists

        # Act
        interactor.react_to_post(user_id=user_id,
                                 post_id=post_id,
                                 reaction_type=reaction_type)

        # Assert
        post_storage.is_valid_post_id.assert_called_once_with(post_id=post_id)
        reaction_storage.create_reaction_to_post.assert_called_once_with(
            user_id=user_id,
            post_id=post_id,
            reaction_type=reaction_type
        )

    def test_react_to_post_interactor_with_undo_post_reaction(self):

        # Arrange
        user_id = 1
        post_id = 1
        reaction_type = ReactionTypeEnum.WOW.value
        post_storage = create_autospec(PostStorageInterface)
        reaction_storage = create_autospec(ReactionStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = ReactToPostInteractor(
            post_storage=post_storage,
            reaction_storage=reaction_storage,
            presenter=presenter
        )

        reaction_storage.validate_post_reaction_if_exists_get_reaction_type. \
            return_value = "WOW"

        # Act
        interactor.react_to_post(user_id=user_id,
                                 post_id=post_id,
                                 reaction_type=reaction_type)

        # Assert
        post_storage.is_valid_post_id.assert_called_once_with(
            post_id=post_id)
        reaction_storage.undo_post_reaction.assert_called_once_with(
            user_id=user_id,
            post_id=post_id)

    def test_react_to_post_interactor_with_update_post_reaction(self):

        # Arrange
        user_id = 1
        post_id = 1
        reaction_type = ReactionTypeEnum.WOW.value
        different_reaction_type = ReactionTypeEnum.LOVE.value
        post_storage = create_autospec(PostStorageInterface)
        reaction_storage = create_autospec(ReactionStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = ReactToPostInteractor(
            post_storage=post_storage,
            reaction_storage=reaction_storage,
            presenter=presenter
        )

        reaction_storage.validate_post_reaction_if_exists_get_reaction_type. \
            return_value = different_reaction_type

        # Act
        interactor.react_to_post(user_id=user_id,
                                 post_id=post_id,
                                 reaction_type=reaction_type)

        # Assert
        post_storage.is_valid_post_id.assert_called_once_with(
            post_id=post_id)
        reaction_storage.update_post_reaction.assert_called_once_with(
            user_id=user_id, post_id=post_id, reaction_type=reaction_type
        )

    def test_react_to_post_interactor_with_invalid_post_id_raise_exception(
            self
    ):

        # Arrange
        user_id = 1
        post_id = -1
        reaction_type = ReactionTypeEnum.WOW.value

        post_storage = create_autospec(PostStorageInterface)
        reaction_storage = create_autospec(ReactionStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = ReactToPostInteractor(
            post_storage=post_storage,
            reaction_storage=reaction_storage,
            presenter=presenter
        )

        post_storage.is_valid_post_id.return_value = False
        presenter.raise_invalid_post_id_exception.side_effect = NotFound

        # Act
        with pytest.raises(NotFound):
            interactor.react_to_post(user_id=user_id,
                                     post_id=post_id,
                                     reaction_type=reaction_type)
