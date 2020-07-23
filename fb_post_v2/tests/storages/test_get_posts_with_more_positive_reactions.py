import pytest

from fb_post_v2.storages.storage_implementation import StorageImplementation

@pytest.mark.django_db
def test_create_reaction_to_comment_with_valid_details(create_users,
                                                       create_posts,
                                                       create_comments,
                                                       create_reactions):

    # Arrange
    expected_post_ids_list = [1]
    storage = StorageImplementation()

    # Act
    actual_post_ids_list = storage.get_posts_with_more_positive_reactions()

    # Assert
    assert actual_post_ids_list == expected_post_ids_list