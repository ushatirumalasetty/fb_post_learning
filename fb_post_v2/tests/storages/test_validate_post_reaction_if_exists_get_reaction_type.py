import pytest

from fb_post_v2.storages.storage_implementation import StorageImplementation

from fb_post_v2.exceptions import ReactionDoesNotExists

@pytest.mark.django_db
def test_validate_post_reaction_if_exists_get_reaction_type_with_valid_details_return_reaction_type(
        create_users, create_posts, create_comments, create_reactions):

    # Arrange
    user_id = 1
    post_id = 1
    expected_reaction_type = "WOW"
    storage = StorageImplementation()

    # Act
    actual_reaction_type = storage. \
        validate_post_reaction_if_exists_get_reaction_type(
            user_id=user_id, post_id=post_id)

    # Assert
    assert actual_reaction_type == expected_reaction_type

@pytest.mark.django_db
def test_validate_post_reaction_if_exists_get_reaction_type_if_reaction_not_exists_raise_exception(
        create_users, create_posts, create_comments, create_reactions):

    # Arrange
    user_id = -1
    post_id = -1
    storage = StorageImplementation()

    # Act
    with pytest.raises(ReactionDoesNotExists):
        storage.validate_post_reaction_if_exists_get_reaction_type(
            user_id=user_id, post_id=post_id
            )
