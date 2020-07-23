import pytest

from fb_post_v2.models import Reaction

from fb_post_v2.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_undo_post_reaction_with_valid_details_delete_reaction(create_users,
                                                               create_posts,
                                                               create_comments,
                                                               create_reactions):

    # Arrange
    user_id = 1
    post_id = 1
    storage = StorageImplementation()

    # Act
    storage.undo_post_reaction(user_id=user_id,
                               post_id=post_id)

    # Assert
    is_reaction_exits =  Reaction.objects.filter(reacted_by_id=user_id,
                                                    post_id=post_id
                                            ).exists()

    assert is_reaction_exits is False
