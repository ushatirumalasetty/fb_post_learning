from unittest.mock import create_autospec

from fb_post_v2.interactors.storages import ReactionStorageInterface

from fb_post_v2.interactors.presenters import PresenterInterface

from fb_post_v2.interactors.get_posts_reacted_by_user_interactor import \
    GetPostsReactedByUserInteractor


class TestGetPostsReactedByUserInteractor:
    
    def test_get_posts_reacted_by_user_interactor(self):

        # Arrange
        user_id = 1
        expected_post_ids_list_mock = [1, 2, 4]
        reaction_storage = create_autospec(ReactionStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetPostsReactedByUserInteractor(
            reaction_storage=reaction_storage, presenter=presenter)

        reaction_storage.get_posts_reacted_by_user.return_value = \
            expected_post_ids_list_mock
        presenter.get_posts_reacted_by_user_response.return_value = \
            expected_post_ids_list_mock

        # Act
        actual_post_ids_list = interactor.get_posts_reacted_by_user(
            user_id=user_id
        )

        # Assert
        assert actual_post_ids_list == expected_post_ids_list_mock
        reaction_storage.get_posts_reacted_by_user.assert_called_once_with(
            user_id=user_id
        )
        presenter.get_posts_reacted_by_user_response.assert_called_once_with(
            post_ids_list=expected_post_ids_list_mock
        )