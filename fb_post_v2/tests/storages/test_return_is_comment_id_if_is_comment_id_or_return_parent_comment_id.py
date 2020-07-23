import pytest

from fb_post_v2.models import Comment

from fb_post_v2.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_return_comment_id_if_is_comment_id_or_return_parent_comment_id_with_comment_id(
        create_users, create_posts, create_comments
):

    # Arrange
    comment_id = 1
    storage = StorageImplementation()

    # Act
    returned_comment_id = storage. \
        return_comment_id_if_is_comment_id_or_return_parent_comment_id(
            comment_id=comment_id
            )

    # Assert
    comment = Comment.objects.get(id=returned_comment_id)

    assert comment.parent_comment_id is None
    assert comment_id == returned_comment_id


@pytest.mark.django_db
def test_return_comment_id_if_is_comment_id_or_return_parent_comment_id_with_reply_id(
        create_users, create_posts, create_comments
):

    # Arrange
    reply_id = 2
    storage = StorageImplementation()

    # Act
    parent_comment_id = storage. \
        return_comment_id_if_is_comment_id_or_return_parent_comment_id(
            comment_id=reply_id
            )

    # Assert
    parent_comment = Comment.objects.get(id=parent_comment_id)

    assert parent_comment.parent_comment_id is None
    assert reply_id != parent_comment_id