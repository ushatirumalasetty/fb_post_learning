from unittest.mock import create_autospec

import pytest

from django_swagger_utils.drf_server.exceptions import NotFound

from fb_post_v2.interactors.storages import ReactionStorageInterface
from fb_post_v2.interactors.storages import CommentStorageInterface

from fb_post_v2.interactors.presenters import PresenterInterface
from fb_post_v2.interactors.react_to_comment_interactor import \
    ReactToCommentInteractor

from fb_post_v2.constants import ReactionTypeEnum

from fb_post_v2.exceptions import ReactionDoesNotExists


class TestReactTocommentInteractor:

    def test_react_to_comment_interactor_with_first_time_react_to_comment(self):

        # Arrange
        user_id = 1
        comment_id = 1
        reaction_type = ReactionTypeEnum.WOW.value
        reaction_storage = create_autospec(ReactionStorageInterface)
        comment_storage = create_autospec(CommentStorageInterface)

        presenter = create_autospec(PresenterInterface)
        interactor = ReactToCommentInteractor(
            comment_storage=comment_storage,
            reaction_storage=reaction_storage,
            presenter=presenter)

        reaction_storage. \
            validate_comment_reaction_if_exists_get_reaction_type. \
            side_effect = ReactionDoesNotExists

        # Act
        interactor.react_to_comment(user_id=user_id,
                                    comment_id=comment_id,
                                    reaction_type=reaction_type)

        # Assert
        comment_storage.is_valid_comment_id.assert_called_once_with(
                 comment_id=comment_id)
        reaction_storage.create_reaction_to_comment.assert_called_once_with(
            user_id=user_id,
            comment_id=comment_id,
            reaction_type=reaction_type
        )


    def test_react_to_comment_interactor_with_undo_comment_reaction(self):

        # Arrange
        user_id = 1
        comment_id = 1
        reaction_type = ReactionTypeEnum.WOW.value
        reaction_storage = create_autospec(ReactionStorageInterface)
        comment_storage = create_autospec(CommentStorageInterface)

        presenter = create_autospec(PresenterInterface)
        interactor = ReactToCommentInteractor(
            reaction_storage=reaction_storage,
            comment_storage=comment_storage,
            presenter=presenter)

        reaction_storage. \
            validate_comment_reaction_if_exists_get_reaction_type. \
                return_value = ReactionTypeEnum.WOW.value

        # Act
        interactor.react_to_comment(user_id=user_id,
                                    comment_id=comment_id,
                                    reaction_type=reaction_type)

        # Assert
        comment_storage.is_valid_comment_id.assert_called_once_with(
            comment_id=comment_id
        )
        reaction_storage.undo_comment_reaction.assert_called_once_with(
            user_id=user_id, comment_id=comment_id
        )


    def test_react_to_comment_interactor_with_update_comment_reaction(self):

        # Arrange
        user_id = 1
        comment_id = 1
        reaction_type = ReactionTypeEnum.WOW.value
        different_reaction_type = ReactionTypeEnum.LOVE.value
        reaction_storage = create_autospec(ReactionStorageInterface)
        comment_storage = create_autospec(CommentStorageInterface)

        presenter = create_autospec(PresenterInterface)
        interactor = ReactToCommentInteractor(
            reaction_storage=reaction_storage,
            comment_storage=comment_storage,
            presenter=presenter)

        reaction_storage. \
            validate_comment_reaction_if_exists_get_reaction_type. \
            return_value = different_reaction_type

        # Act
        interactor.react_to_comment(user_id=user_id,
                                    comment_id=comment_id,
                                    reaction_type=reaction_type)

        # Assert
        comment_storage.is_valid_comment_id.assert_called_once_with(
            comment_id=comment_id
        )
        reaction_storage.update_comment_reaction.assert_called_once_with(
            user_id=user_id, comment_id=comment_id, reaction_type=reaction_type
        )


    def test_react_to_comment_interactor_with_invalid_comment_id_raise_exception(
            self
    ):

        # Arrange
        user_id = 1
        comment_id = -1
        reaction_type = ReactionTypeEnum.WOW.value
        reaction_storage = create_autospec(ReactionStorageInterface)
        comment_storage = create_autospec(CommentStorageInterface)

        presenter = create_autospec(PresenterInterface)
        interactor = ReactToCommentInteractor(
            reaction_storage=reaction_storage,
            comment_storage=comment_storage,
            presenter=presenter)

        comment_storage.is_valid_comment_id.return_value = False 
        presenter.raise_invalid_comment_id_exception.side_effect = NotFound

        # Act
        with pytest.raises(NotFound):
            interactor.react_to_comment(user_id=user_id,
                                        comment_id=comment_id,
                                        reaction_type=reaction_type)
