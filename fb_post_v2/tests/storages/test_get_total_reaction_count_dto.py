import pytest

from fb_post_v2.models import Reaction

from fb_post_v2.storages.storage_implementation import StorageImplementation

from fb_post_v2.constants import ReactionTypeEnum 

from fb_post_v2.interactors.storages.dtos import TotalReactionCountDto

@pytest.mark.django_db
def test_get_total_reaction_count_dto_with_valid_details_return_dto(
        create_users, create_posts, create_comments, create_reactions
):

    # Arrange
    expected_total_reaction_count_dto = TotalReactionCountDto(count=2) 
    storage = StorageImplementation()

    # Act
    
    actual_total_reation_count_dto = storage.get_total_reaction_count_dto()

    # Assert
    assert actual_total_reation_count_dto.count == \
        expected_total_reaction_count_dto.count

    assert actual_total_reation_count_dto == \
        expected_total_reaction_count_dto
    