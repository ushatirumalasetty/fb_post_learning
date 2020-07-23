"""
from django.db.models import Count, Q
from fb_post.models import Post, Reaction
from fb_post.constants import ReactionChoices
from fb_post.exceptions import (
    UserCannotDeletePostException,
    InvalidPostException
    )
from .utils_validators import (
    is_valid_post_content,
    is_valid_user,
    is_valid_post
    )


# 7
def get_total_reaction_count():
    reaction_count_dict = Reaction.objects\
                                  .aggregate(
                                      count=Count('reacted_by')
                                  )

    return reaction_count_dict


# 8
def get_reaction_metrics(post_id):

    is_post_id_valid(post_id)

    reactions_with_counts_in_list = Reaction.objects\
                                         .filter(post_id=post_id)\
                                         .values_list('reaction')\
                                         .annotate(
                                             count=Count('reaction')
                                         )

    reactions_dict = {}
    for react_touple in reactions_with_counts_in_list:
        reactions_dict[react_touple[0]] = react_touple[1]

    return reactions_dict


# 9
def delete_post(user_id, post_id):

    is_user_id_valid(user_id)

    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise InvalidPostException

    if post.posted_by_id != user_id:
        raise UserCannotDeletePostException

    post.delete()

def get_postive_reactions_list():

    positive_reactions = [ReactionChoices.WOW.value,
                          ReactionChoices.LIT.value,
                          ReactionChoices.LOVE.value,
                          ReactionChoices.HAHA.value,
                          ReactionChoices.THUMBS_UP.value
                          ]

    return positive_reactions


def get_negative_reactions_list():
    negative_reactions = [ReactionChoices.THUMBS_DOWN.value,
                          ReactionChoices.ANGRY.value,
                          ReactionChoices.SAD.value,
                          ]

    return negative_reactions


# 10
def get_posts_with_more_positive_reactions():

    positive_reactions = get_postive_reactions_list()
    negative_reactions = get_negative_reactions_list()

    positive_reactions_count = Count('reaction',
                                     filter=Q(
                                         reaction__in=positive_reactions)
                                    )
    negative_reactions_count = Count('reaction',
                                     filter=Q(
                                         reaction__in=negative_reactions)
                                    )

    return list(Reaction.objects.select_related('post')\
                        .values('post_id')\
                        .annotate(
                            positive_reactions_count=positive_reactions_count,
                            negative_reactions_count=negative_reactions_count)\
                        .filter(
                            no_of_positive_count__gt=negative_reactions_count)\
                        .values_list('post_id', flat=True)
               )


# 11
def get_posts_reacted_by_user(user_id):

    is_user_id_valid(user_id)

    return list(Post.objects.filter(posted_by_id=user_id)\
                    .values_list('id', flat=True)
               )


def get_user_with_reaction_in_dict(react):
    return {
        'user_id':react.reacted_by.id,
        'name':react.reacted_by.name,
        'profile_pic':react.reacted_by.profile_pic,
        'reaction':react.reaction
        }


# 12
def get_reactions_to_post(post_id):

    is_post_id_valid(post_id)

    reactions_queryset = Reaction.objects.filter(post_id=post_id)\
                                 .select_related('reacted_by')

    post_reactions = []
    for reaction in reactions_queryset:
        user_dict = get_user_with_reaction_in_dict(reaction)
        post_reactions.append(user_dict)

    return post_reactions
"""