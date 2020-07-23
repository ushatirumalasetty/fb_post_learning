import pytest

from fb_post_v2.models import Reaction

from fb_post_v2.storages.storage_implementation import StorageImplementation

from fb_post_v2.constants import ReactionTypeEnum 

@pytest.mark.django_db
def test_create_reaction_to_post_with_valid_details(create_users,
                                                    create_posts,
                                                    create_comments,
                                                    create_reactions):

    # Arrange
    user_id = 1
    post_id = 1
    reaction_type = ReactionTypeEnum.LIT.value
    storage = StorageImplementation()

    # Act
    
    reaction_id = storage.create_reaction_to_post(user_id=user_id,
                                                  post_id=post_id,
                                                  reaction_type=reaction_type)

    # Assert
    reaction = Reaction.objects.get(id=reaction_id)

    assert reaction_id == reaction.id