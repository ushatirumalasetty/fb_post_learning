import pytest

from fb_post_v2.models import Comment

from fb_post_v2.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_reply_to_comment_with_valid_details_return_reply_id(create_users,
                                                             create_posts,
                                                             create_comments):

    # Arrange
    user_id = 1
    comment_id = 1
    reply_content = 'Reply Content'
    storage = StorageImplementation()

    # Act
    reply_id = storage.reply_to_comment(user_id=user_id,
                                        comment_id=comment_id,
                                        reply_content=reply_content)

    # Assert
    reply = Comment.objects.get(id=reply_id)

    assert reply_id == reply.id
