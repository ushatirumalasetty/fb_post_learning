import pytest

from fb_post_v2.models import Comment

from fb_post_v2.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_create_comment_with_valid_details_returns_comment_id(
        create_users,
        create_posts):

    # Arrange
    user_id = 1
    post_id = 1
    comment_content = 'Comment content'
    storage = StorageImplementation()

    # Act
    comment_id = storage.create_comment(user_id=user_id,
                                        post_id=post_id,
                                        comment_content=comment_content)

    # Assert
    comment = Comment.objects.get(id=comment_id)

    assert comment_id== comment.id
