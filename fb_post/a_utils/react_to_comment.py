import datetime
from fb_post.models import Reaction
from fb_post.constants import ReactionChoices
from fb_post.exceptions import InvalidReactionTypeException
from .utils_validators import (
    is_valid_user,
    is_valid_comment
    )


def is_invalid_reaction_type(reaction_type):
    reaction_choices = get_reaction_choices_list()

    if reaction_type not in reaction_choices:
        return True
    return False


def get_reaction_choices_list():

    return [ReactionChoices.WOW.value,
            ReactionChoices.LIT.value,
            ReactionChoices.LOVE.value,
            ReactionChoices.HAHA.value,
            ReactionChoices.THUMBS_UP.value,
            ReactionChoices.THUMBS_DOWN.value,
            ReactionChoices.ANGRY.value,
            ReactionChoices.SAD.value
            ]


def is_reaction_exists(reaction):

    if reaction.exists():
        return True
    return False


def is_reaction_types_same(reaction, reaction_type):

    if reaction.reaction == reaction_type:
        return True
    return False


def is_reaction_type_are_different(reaction, reaction_type):

    return reaction.reaction != reaction_type


def update_or_delete_reaction(reaction, reaction_type):

    if is_reaction_types_same(reaction[0], reaction_type):# TODO: remove indexing
        reaction.delete()

    elif is_reaction_type_are_different(reaction[0], reaction_type):
        reaction.update(reaction=reaction_type,
                        reacted_at=datetime.datetime.now())


# 6
def react_to_comment(user_id, comment_id, reaction_type):

    is_valid_user(user_id)
    is_valid_comment(comment_id)

    if is_invalid_reaction_type(reaction_type):
        raise InvalidReactionTypeException

    reaction = Reaction.objects.filter(comment_id=comment_id,
                                       reacted_by_id=user_id)
    len(reaction)

    if is_reaction_exists(reaction):
        update_or_delete_reaction(reaction, reaction_type)

    else:
        Reaction.objects.create(comment_id=comment_id,
                                reacted_by_id=user_id,
                                reaction=reaction_type)
