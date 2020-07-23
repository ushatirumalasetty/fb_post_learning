from django.db.models import Count, Q
from fb_post.constants import ReactionChoices
from fb_post.models import  Reaction


def get_postive_reactions_list():

    positive_reactions = [ReactionChoices.WOW.value,
                          ReactionChoices.LIT.value,
                          ReactionChoices.LOVE.value,
                          ReactionChoices.HAHA.value,
                          ReactionChoices.THUMBS_UP.value
                          ]

    return positive_reactions


def get_negative_reactions_list(): # use in constants
    negative_reactions = [ReactionChoices.THUMBS_DOWN.value,
                          ReactionChoices.ANGRY.value,
                          ReactionChoices.SAD.value
                          ]

    return negative_reactions


def get_postive_reaction_count():
    positive_reactions = get_postive_reactions_list()

    positive_reactions_count = Count('reaction',
                                     filter=Q(
                                         reaction__in=positive_reactions)
                                    )
    return positive_reactions_count


def get_negative_reactions_count():
    negative_reactions = get_negative_reactions_list()

    negative_reactions_count = Count('reaction',
                                     filter=Q(
                                         reaction__in=negative_reactions)
                                    )
    return negative_reactions_count


# 10
def get_posts_with_more_positive_reactions():

    positive_reactions_count = get_postive_reaction_count()
    negative_reactions_count = get_negative_reactions_count()

    return list(Reaction.objects.select_related('post')\
                        .values('post_id')\
                        .annotate(
                            positive_reactions_count=positive_reactions_count,
                            negative_reactions_count=negative_reactions_count)\
                        .filter(
                            positive_reactions_count__gt=(
                                negative_reactions_count)
                                )\
                        .values_list('post_id', flat=True)
               )

