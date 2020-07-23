import pytest

from fb_post_v2.models import Reaction

from fb_post_v2.storages.storage_implementation import StorageImplementation

from fb_post_v2.constants import ReactionTypeEnum 

from  fb_post_v2.interactors.storages.dtos import PostCompleteDetailsDto

@pytest.mark.django_db
def test_get_post_dto_with_valid_details_return_dto(create_users,
                                                    create_posts,
                                                    get_post_create_comments,
                                                    create_reactions,
                                                    get_post_user_dtos,
                                                    get_post_comment_dtos,
                                                    get_post_reaction_dtos,
                                                    get_post_post_dto):

    # Arrange
    post_id = 1
    expected = PostCompleteDetailsDto(post_dto=get_post_post_dto,
                                      user_dtos=get_post_user_dtos,
                                      comment_dtos=get_post_comment_dtos,
                                      reaction_dtos=get_post_reaction_dtos)
    storage = StorageImplementation()

    # Act
    actual_post_complete_dto = storage.get_post_dto(post_id=post_id)

    # Assert
    assert actual_post_complete_dto == expected 