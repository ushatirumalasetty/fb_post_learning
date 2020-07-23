import pytest

from fb_post_v2.models import Post

from fb_post_v2.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_create_post_with_valid_details_returns_post_id(create_users):

    # Arrange
    user_id = 1
    post_content = 'Post content'
    storage = StorageImplementation()

    # Act
    post_id = storage.create_post(user_id=user_id,
                                  post_content=post_content)

    # Assert
    post = Post.objects.get(id=post_id)

    assert post_id == post.id