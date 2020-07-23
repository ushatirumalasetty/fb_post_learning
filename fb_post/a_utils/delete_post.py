from fb_post.validators.exceptions import UserCannotDeletePostException
from fb_post.validators.validators import (
    is_valid_user,
    is_valid_post
)


# 9
def delete_post(user_id, post_id):

    is_valid_user(user_id)
    post = is_valid_post(post_id)

    is_valid_user_to_delete_post = post.posted_by_id == user_id #TODO: variable naming - done
    if is_valid_user_to_delete_post:
        post.delete()
    else:
        raise UserCannotDeletePostException 
