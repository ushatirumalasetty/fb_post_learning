import pytest

from fb_post_v2.models import Reaction

from fb_post_v2.storages.storage_implementation import StorageImplementation

from fb_post_v2.constants import ReactionTypeEnum 

from fb_post_v2.interactors.storages.dtos import ReactionMetricsDto


@pytest.mark.django_db
def test_get_reaction_metrics_dto_with_valid_details_returrn_dto(
        create_users,
        create_posts,
        create_comments,
        create_reactions
):

    # Arrange
    post_id = 1
    expected_reaction_metrics_dtos = [
        ReactionMetricsDto(
            reaction_type=ReactionTypeEnum.WOW.value,
            count=1
        )
    ]
    storage = StorageImplementation()

    # Act
    actual_reaction_metrics_dtos = storage.get_reaction_metrics_dto(
        post_id=post_id
    )

    # Assert
    assert actual_reaction_metrics_dtos[0].reaction_type == \
        expected_reaction_metrics_dtos[0].reaction_type
    assert actual_reaction_metrics_dtos[0].count == \
        expected_reaction_metrics_dtos[0].count
    assert actual_reaction_metrics_dtos == expected_reaction_metrics_dtos