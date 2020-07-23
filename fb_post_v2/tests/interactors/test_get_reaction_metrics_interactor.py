from unittest.mock import create_autospec

from fb_post_v2.interactors.storages import PostStorageInterface
from fb_post_v2.interactors.storages import ReactionStorageInterface

from fb_post_v2.interactors.presenters import \
    PresenterInterface

from fb_post_v2.interactors.get_reaction_metrics_interactor import \
    GetReactionMetricsInteractor

import pytest

from django_swagger_utils.drf_server.exceptions import NotFound


class TestGetReactionMetricsInteractor:
    
    def test_get_reaction_metrics_with_valid_details(
        self, reactions_metrics_dtos, get_reactions_metrics_dto_response
    ):

        # Arrange
        post_id = 1
        expected_reaction_metrics_dict_mock = \
            get_reactions_metrics_dto_response
        post_storage = create_autospec(PostStorageInterface)
        reaction_storage = create_autospec(ReactionStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetReactionMetricsInteractor(
                post_storage=post_storage,
                reaction_storage=reaction_storage,
                presenter=presenter)

        reaction_storage.get_reaction_metrics_dto.return_value = \
            reactions_metrics_dtos
        presenter.get_reaction_metrics_response.return_value = \
            expected_reaction_metrics_dict_mock

        # Act
        actual_reaction_metrics_dict = interactor.get_reaction_metrics(
            post_id=post_id
        )

        # Assert
        assert actual_reaction_metrics_dict == \
            expected_reaction_metrics_dict_mock
        post_storage.is_valid_post_id.assert_called_once_with(post_id=post_id)
        reaction_storage.get_reaction_metrics_dto.assert_called_once_with(
            post_id=post_id
        )
        presenter.get_reaction_metrics_response.assert_called_once_with(
            get_reaction_metrics_dto=reactions_metrics_dtos
        )


    def test_get_reaction_metrics_interactor_with_invalid_post_id(self):

        # Arrange
        post_id = -1
        post_storage = create_autospec(PostStorageInterface)
        reaction_storage = create_autospec(ReactionStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetReactionMetricsInteractor(
                post_storage=post_storage,
                reaction_storage=reaction_storage,
                presenter=presenter)

        post_storage.is_valid_post_id.return_value = False
        presenter.raise_invalid_post_id_exception.side_effect = NotFound

        # Act
        with pytest.raises(NotFound):
            interactor.get_reaction_metrics(post_id=post_id)