import pytest

from fb_post_v2.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_is_valid_comment_id_with_valid_details_return_true(create_users,
                                                            create_posts,
                                                            create_comments):

    # Arrange
    comment_id = 1
    storage = StorageImplementation()

    # Act
    is_valid_comment_id = storage.is_valid_comment_id(comment_id=comment_id)

    # Assert
    assert is_valid_comment_id is True


@pytest.mark.django_db
def test_is_valid_comment_id_with_invalid_details_return_false(create_users,
                                                               create_posts,
                                                               create_comments):

    # Arrange
    invali_comment_id = -1
    storage = StorageImplementation()

    # Act
    is_valid_comment_id = storage.is_valid_comment_id(
            comment_id=invali_comment_id
    )

    # Assert
    assert is_valid_comment_id is False