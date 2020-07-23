import pytest

from fb_post_v2.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_get_posts_reacted_by_with_valid_details_return_ids_list(
        create_users,
        create_posts,
        create_comments,
        create_reactions
):

    # Arrange
    user_id = 1
    expected_post_ids_list = [1]
    storage = StorageImplementation()

    # Act
    actual_post_ids_list = storage.get_posts_reacted_by_user(user_id=user_id)

    # Assert
    assert actual_post_ids_list.sort() == expected_post_ids_list.sort()