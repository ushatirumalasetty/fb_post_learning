from fb_post.models.comment import Comment
from fb_post.validators.validators import (
    is_valid_comment_content,
    is_valid_user,
    is_valid_post
)


# 3
def create_comment(user_id, post_id, comment_content):

    is_valid_comment_content(comment_content)
    is_valid_user(user_id)
    is_valid_post(post_id) #TODO: is_valid_post_id - done

    comment = Comment.objects.create(content=comment_content,
                                     post_id=post_id,
                                     commented_by_id=user_id)

    return comment.id
