import datetime
from fb_post.models import Reaction
from .react_to_comment import is_invalid_reaction_type
from .utils_validators import is_valid_user, is_valid_post
from fb_post.exceptions import InvalidReactionTypeException
from fb_post.constants import ReactionChoices


def is_user_already_reacted_to_post(reaction):
    if reaction.exists():
        return True
    return False


def is_invalid_reaction_type(reaction_type):
    reaction_choices = get_reaction_choices_list()

    if reaction_type.upper() not in reaction_choices:
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

    if reaction.reaction != reaction_type:
        return True
    return False


def update_or_delete_reaction(reaction, reaction_type):

    if is_reaction_types_same(reaction.first(), reaction_type):
        reaction.delete()

    elif is_reaction_type_are_different(reaction.first(), reaction_type):
        reaction.update(reaction=reaction_type,
                        reacted_at=datetime.datetime.now())


# 5
def react_to_post(user_id, post_id, reaction_type):

    is_invalid_reaction_type(reaction_type) #TODO: is_valid_reaction_type
    is_valid_user(user_id)
    is_valid_post(post_id)

    reaction = Reaction.objects.filter(post_id=post_id, reacted_by_id=user_id)

    if is_invalid_reaction_type(reaction_type):
        raise InvalidReactionTypeException

    if is_user_already_reacted_to_post(reaction):
        update_or_delete_reaction(reaction, reaction_type)
    else:
        Reaction.objects.create(post_id=post_id,
                                reacted_by_id=user_id,
                                reaction=reaction_type)
