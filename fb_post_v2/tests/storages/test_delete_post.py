import pytest

from fb_post_v2.models import Post

from fb_post_v2.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_delete_post_with_valid_details(create_users,
                                        create_posts):

    # Arrange
    post_id = 1
    storage = StorageImplementation()

    # Act
    storage.delete_post(post_id=post_id)

    # Assert
    is_post_exists = Post.objects.filter(id=post_id).exists()
    is_post_deleted = not is_post_exists

    assert is_post_deleted is True