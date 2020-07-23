from fb_post.models import Reaction
from .utils_validators import is_valid_post


def get_user_with_reaction_in_dict(react):
    return {
        'user_id':react.reacted_by.id,
        'name':react.reacted_by.name,
        'profile_pic':react.reacted_by.profile_pic,
        'reaction':react.reaction
        }

# 12
def get_reactions_to_post(post_id):

    is_valid_post(post_id)

    reactions_objs = Reaction.objects.filter(post_id=post_id)\
                                 .select_related('reacted_by')

    post_reactions_list = [
        get_user_with_reaction_in_dict(reaction)
        for reaction in reactions_objs
    ]

    return post_reactions_list
