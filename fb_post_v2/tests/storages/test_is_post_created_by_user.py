import pytest

from fb_post_v2.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_is_post_created_by_user_with_valid_details_return_true(
        create_users, create_posts, create_comments, create_reactions
):

    # Arrange
    user_id = 1
    post_id = 1
    storage = StorageImplementation()

    # Act
    is_post_created_by_user = storage.is_post_created_by_user(user_id=user_id,
                                                              post_id=post_id)
    # Assert
    assert is_post_created_by_user is True


@pytest.mark.django_db
def test_is_post_created_by_user_with_invalid_details_return_false(
        create_users, create_posts, create_comments, create_reactions
):

    # Arrange
    invalid_user_id = -1
    post_id = 1
    storage = StorageImplementation()

    # Act
    is_post_created_by_user = storage.is_post_created_by_user(
        user_id=invalid_user_id, post_id=post_id)

    # Assert
    assert is_post_created_by_user is False