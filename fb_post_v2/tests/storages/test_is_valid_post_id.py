import pytest

from fb_post_v2.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_is_valid_post_id_with_valid_details_returns_true(
        create_users,
        create_posts):

    # Arrange
    post_id = 1
    storage = StorageImplementation()

    # Act
    is_valid_post_id = storage.is_valid_post_id(post_id=post_id)

    # Assert
    assert is_valid_post_id is True


@pytest.mark.django_db
def test_is_valid_post_id_with_invalid_details_returns_false(
        create_users,
        create_posts):

    # Arrange
    invalid_post_id = -1
    storage = StorageImplementation()

    # Act
    is_valid_post_id = storage.is_valid_post_id(post_id=invalid_post_id)

    # Assert
    assert is_valid_post_id is False
