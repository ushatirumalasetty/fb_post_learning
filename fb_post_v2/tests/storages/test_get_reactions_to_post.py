import pytest

from fb_post_v2.models import Reaction

from fb_post_v2.storages.storage_implementation import StorageImplementation

from fb_post_v2.constants import ReactionTypeEnum

from fb_post_v2.interactors.storages.dtos import PostReactionsDto, UserDto


@pytest.mark.django_db
def test_get_reactions_to_post_dto_with_valid_details_return_dto(
        create_users,
        create_posts,
        create_comments,
        create_post_reactions
):

    # Arrange
    post_id = 1
    user_dto1 = UserDto(user_id=1,
                        name="che",
                        profile_pic="che/profile_pic")
    user_dto2 = UserDto(user_id=2,
                        name="stevejobs",
                        profile_pic="stevjobs/profile_pic")

    expected_post_reaction_dtos = [
        PostReactionsDto(user_dto=user_dto1,
                         reaction=ReactionTypeEnum.WOW.value),
        PostReactionsDto(user_dto=user_dto2,
                         reaction=ReactionTypeEnum.LOVE.value)]

    storage = StorageImplementation()

    # Act
    actual_post_reaction_dtos = storage.get_reactions_to_post_dto(
        post_id=post_id
    )

    # Assert
    assert actual_post_reaction_dtos == expected_post_reaction_dtos
