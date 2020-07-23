from collections import defaultdict
from .utils_dicts import get_post_dict, get_comment_dict


#TODO: change functions to separate module
def mapping_comment_with_replies_dict(post):# names not revealing the name -done

    post_comments_list = post.comment_set.all()
    comment_with_replies_dict = defaultdict(list)

    for comment in post_comments_list:
        is_comment = comment.parent_comment_id is None # variable name is comment
        if is_comment:
            comment_with_replies_dict[comment] = (
                filter_replies_for_comment(comment, post_comments_list))
    return comment_with_replies_dict


def filter_replies_for_comment(comment, replies):# change function names
    comment_replies_list = [
        reply for reply in replies if is_reply_for_given_comment(
            comment,reply)
        ]
    return comment_replies_list


def is_reply_for_given_comment(comment,reply):
    return reply.parent_comment_id == comment.id


def get_replies_dict_list(replies):
    replies_dict_list = [
        get_comment_dict(reply) for reply in replies 
        ]
    return replies_dict_list


def get_comments_dict_list(comment, comment_repplies_list):

    comment_dict_with_replies = get_comment_dict(comment)
    comment_dict_with_replies['replies_count'] = len(comment_repplies_list)#
    comment_dict_with_replies['replies'] = comment_repplies_list

    return comment_dict_with_replies


def get_comment_details_dict(comment_with_replies): #change function name
    comments_dict_along_with_replies_list = []

    for comment, replies in comment_with_replies.items():
        replies_dict_list = get_replies_dict_list(replies)
        comments_dict_along_with_replies_list.append(
            get_comments_dict_list(comment, replies_dict_list))

    return comments_dict_along_with_replies_list


def get_post_details_dict(post_obj):

    post_comments_with_replies_dict = mapping_comment_with_replies_dict(
        post_obj
    )

    comments_with_all_details_list = get_comment_details_dict(
        post_comments_with_replies_dict)

    post_dict = get_post_dict(post_obj)
    post_dict['comments'] = comments_with_all_details_list
    post_dict['comments_count'] = len(comments_with_all_details_list)

    return post_dict
