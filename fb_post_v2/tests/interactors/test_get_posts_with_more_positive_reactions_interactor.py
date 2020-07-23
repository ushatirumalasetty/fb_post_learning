from unittest.mock import create_autospec

from fb_post_v2.interactors.storages import ReactionStorageInterface

from fb_post_v2.interactors.presenters import PresenterInterface

from fb_post_v2.interactors.get_posts_with_more_positive_reactions_interactor \
    import GetPostsWithMorePositiveReactionsInteractor


class TestGetPostsWithMorePositiveReactionsInteractor:

    def test_get_posts_with_more_positive_reactions_interactor(self):

        # Arrange
        expected_post_ids_list_mock = [1, 2, 3]
        reaction_storage = create_autospec(ReactionStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetPostsWithMorePositiveReactionsInteractor(
            reaction_storage=reaction_storage,
            presenter=presenter
        )

        reaction_storage.get_posts_with_more_positive_reactions.return_value = \
            expected_post_ids_list_mock
        presenter.get_posts_with_more_positive_reactions_response. \
            return_value = expected_post_ids_list_mock

        # Act
        actual_post_ids_list = \
            interactor.get_posts_with_more_positive_reactions()

        # Assert
        assert actual_post_ids_list == expected_post_ids_list_mock
        reaction_storage. \
            get_posts_with_more_positive_reactions.assert_called_once()
        presenter.get_posts_with_more_positive_reactions_response. \
            assert_called_once_with(
                post_ids_list=expected_post_ids_list_mock
            )
