from fb_post.models import Comment
from .utils_validators import is_valid_comment
from .utils_dicts import get_user_dict, get_date_time


def get_reply_dict(reply):

    reply_user_dict = get_user_dict(reply.commented_by)
    replied_date_time = get_date_time_as_string(reply.commented_at)

    return {
        "comment_id": reply.id,
        "commenter": reply_user_dict,
        "commented_at": replied_date_time,
        "comment_content": reply.content
    }


def get_replies_for_comment(comment_id):

    is_valid_comment(comment_id)

    comment_replies = Comment.objects.filter(parent_comment_id=comment_id)\
                             .select_related('commented_by')

    replies_dict_in_list = []
    #TODO: list comprehension
    for reply in comment_replies:
        replies_dict_in_list.append(get_reply_dict(reply))

    return replies_dict_in_list
