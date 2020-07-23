from unittest.mock import create_autospec

from fb_post_v2.interactors.storages import PostStorageInterface
from fb_post_v2.interactors.presenters import PresenterInterface
from fb_post_v2.interactors.create_post_interactor import CreatePostInteractor


def test_create_post_interactor_with_valid_details():

    # Arrange
    user_id = 1
    post_content = 'New Post'
    expected_post_id = 1
    expected_post_id_dict = {
        'post_id': expected_post_id
    }
    post_storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreatePostInteractor(post_storage=post_storage,
                                      presenter=presenter)

    post_storage.create_post.return_value = expected_post_id
    presenter.get_create_post_response.return_value = expected_post_id_dict

    # Act
    actual_post_id_dict = interactor.create_post(user_id=user_id,
                                                 post_content=post_content)

    # Arrange
    assert actual_post_id_dict == expected_post_id_dict
    post_storage.create_post.assert_called_once_with(user_id=user_id,
                                                     post_content=post_content)
    presenter.get_create_post_response.assert_called_once_with(
        post_id=expected_post_id
    )