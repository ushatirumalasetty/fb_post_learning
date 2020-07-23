from unittest.mock import create_autospec

from fb_post_v2.interactors.storages import PostStorageInterface
from fb_post_v2.interactors.storages import ReactionStorageInterface

from fb_post_v2.interactors.presenters import PresenterInterface

from fb_post_v2.interactors.get_reactions_to_post_interactor import \
    GetReactionsToPostInteractor

import pytest

from fb_post_v2.constants import ReactionTypeEnum

from fb_post_v2.interactors.storages.dtos import PostReactionsDto

from django_swagger_utils.drf_server.exceptions import NotFound


class TestGetReactionsToPostInteractor:
    def test_get_reactions_to_post_interactor(self,
                                              user_dto,
                                              get_post_reactions_dto_response):

        # Arrange
        post_id = 1
        expected_reactions_dict_list_mock = get_post_reactions_dto_response

        post_storage = create_autospec(PostStorageInterface)
        reaction_storage = create_autospec(ReactionStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetReactionsToPostInteractor(
            post_storage=post_storage,
            reaction_storage=reaction_storage,
            presenter=presenter
        )

        get_post_reaction_dto = [
            PostReactionsDto(user_dto=user_dto,
                             reaction=ReactionTypeEnum.WOW.value)
        ]

        reaction_storage.get_reactions_to_post_dto.return_value = \
            get_post_reaction_dto
        presenter.get_reactions_to_post_response.return_value = \
            expected_reactions_dict_list_mock

        
        # Act
        actual_reactions_dict_list = interactor.get_reactions_to_post(
            post_id=post_id
        )

        # Assert
        assert actual_reactions_dict_list == \
            expected_reactions_dict_list_mock
        reaction_storage.get_reactions_to_post_dto.assert_called_once_with(
            post_id=post_id
        )
        presenter.get_reactions_to_post_response.assert_called_once_with(
            get_post_reaction_dto=get_post_reaction_dto
        )
        post_storage.is_valid_post_id.assert_called_once_with(post_id=post_id)


    def test_get_reactions_to_post_interactor_with_invalid_post_id_raise_exception(
        self
    ):

        # Arrange
        invalid_post_id = -1
        post_storage = create_autospec(PostStorageInterface)
        reaction_storage = create_autospec(ReactionStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetReactionsToPostInteractor(
            post_storage=post_storage,
            reaction_storage=reaction_storage,
            presenter=presenter
        )
        
        post_storage.is_valid_post_id.return_value = False
        presenter.raise_invalid_post_id_exception.side_effect = NotFound
        
        # Act
        with pytest.raises(NotFound):
            interactor.get_reactions_to_post(
                post_id=invalid_post_id
            )

