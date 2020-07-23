from django.utils import timezone
import pytest
from django.db.models import Count
from fb_post.models import Reaction
from .utils_checks import (
    is_valid_post
    )


# 8
def get_reaction_metrics(post_id):

    is_valid_post(post_id)

    #TODO: code formatting
    reactions_with_counts_in_list = Reaction.objects\
                                            .filter(post_id=post_id)\
                                         .values_list('reaction')\
                                         .annotate(
                                             count=Count('reaction')
                                         )

    reactions_dict = {}
    #TODO: use dict
    for react_touple in reactions_with_counts_in_list:
        reactions_dict[react_touple[0]] = react_touple[1]

    return reactions_dict
