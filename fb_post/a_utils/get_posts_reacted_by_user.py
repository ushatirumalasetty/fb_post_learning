from fb_post.models.post import Post
from fb_post.validators.validators import is_valid_user


# 11
def get_posts_reacted_by_user(user_id):

    is_valid_user(user_id)
    user_reacted_post_ids_list = list(Post.objects
                                          .filter(posted_by_id=user_id)\
                                          .values_list('id', flat=True)
                                     ) # assign the query to variable  -done

    return user_reacted_post_ids_list