from fb_post.models import Post
from .utils_validators import (
    is_valid_user,
    is_valid_post_content
)


def create_post(user_id, post_content):

    is_valid_user(user_id)
    is_valid_post_content(post_content)

    post = Post.objects.create(posted_by_id=user_id,
                               content=post_content)

    return post.id
