from unittest.mock import create_autospec

from fb_post_v2.interactors.storages import ReactionStorageInterface

from fb_post_v2.interactors.presenters import PresenterInterface

from fb_post_v2.interactors.get_total_reaction_count_interactor import \
    GetTotalReactionCountInteractor


class TestGetTotalReactionCountInteractor:

    def test_get_total_reaction_count_interactor(
            self,
            get_total_reaction_count_dto,
            get_total_reaction_count_dto_response
    ):

        # Arrange
        expected_count_dict_mock = get_total_reaction_count_dto_response
        reaction_storage = create_autospec(ReactionStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetTotalReactionCountInteractor(
            reaction_storage=reaction_storage, presenter=presenter)

        reaction_storage.get_total_reaction_count_dto.return_value = \
            get_total_reaction_count_dto
        presenter.get_total_reaction_count_response.return_value = \
            expected_count_dict_mock

        # Act
        actual_count_dict = interactor.get_total_reaction_count()

        # Assert
        assert actual_count_dict == expected_count_dict_mock
        reaction_storage.get_total_reaction_count_dto.assert_called_once()
        presenter.get_total_reaction_count_response.assert_called_once_with(
            get_total_reaction_count_dto= get_total_reaction_count_dto
        )

