

def get_user_dict(user):

    return {
        "user_id": user.id,
        "name": user.name,
        "profile_pic": user.profile_pic
    }


def get_reaction_list(reactions_list):

    unique_reactions_list = []
    for reaction in reactions_list:
        unique_reactions_list.append(reaction.reaction)

    count = len(unique_reactions_list)
    reaction_type_list = list(set(unique_reactions_list))

    reactions_dict = {
        'count': count,
        'type': reaction_type_list
        }
    return reactions_dict


def get_date_time(date_time):
    return date_time.strftime('%Y-%m-%d %H:%M:%S.%f')


def get_comment_dict(comment):

    reactions = get_reaction_list(list(comment.reaction_set.all()))
    comment_user_dict = get_user_dict(comment.commented_by)
    date_time = get_date_time(comment.commented_at)

    comment_dict = {
                "comment_id": comment.id,
                "commenter": comment_user_dict,
                "commented_at": date_time,
                "comment_content": comment.content,
                "reactions": reactions
    }

    return comment_dict


def get_post_dict(post):

    reactions = get_reaction_list(list(post.reaction_set.all()))
    post_user_dict = get_user_dict(post.posted_by)
    date_time = get_date_time(post.posted_at)

    post_dict = {
                "post_id": post.id,
                "posted_by": post_user_dict,
                "posted_at": date_time,
                "post_content": post.content,
                "reactions": reactions
    }

    return post_dict
