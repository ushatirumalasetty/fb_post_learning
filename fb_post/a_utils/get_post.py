from django.db.models import Prefetch
from fb_post.models.post import Post
from fb_post.models.comment import Comment
from fb_post.validators.validators import is_valid_post
from .get_post_details_dict import get_post_details_dict


# 13
def get_post(post_id=None):

    is_valid_post(post_id)

    comment_query_set = Comment.objects\
                               .select_related('commented_by')\
                               .prefetch_related('reaction_set')

    post_obj = Post.objects\
                   .select_related('posted_by')\
                   .prefetch_related(
                       'reaction_set',
                       Prefetch(
                           'comment_set',
                           queryset=comment_query_set)
                   ).get(pk=post_id)

    return get_post_details_dict(post_obj)
