from fb_post_v2.interactors.storages import PostStorageInterface
from fb_post_v2.interactors.storages import ReactionStorageInterface

from fb_post_v2.interactors.presenters import PresenterInterface

from fb_post_v2.constants import ReactionTypeEnum

from fb_post_v2.exceptions import ReactionDoesNotExists


class ReactToPostInteractor:

    def __init__(self,
                 post_storage: PostStorageInterface,
                 reaction_storage: ReactionStorageInterface,
                 presenter: PresenterInterface):

        self.post_storage = post_storage
        self.reaction_storage = reaction_storage
        self.presenter = presenter

    def react_to_post(self,
                      user_id: int,
                      post_id: int,
                      reaction_type: ReactionTypeEnum):

        is_valid_post_id = self.post_storage.is_valid_post_id(post_id=post_id)
        invalid_post_id_given = not is_valid_post_id

        if invalid_post_id_given:
            self.presenter.raise_invalid_post_id_exception()
            return

        try:
            old_reaction_type = self.reaction_storage. \
                validate_post_reaction_if_exists_get_reaction_type(
                    user_id=user_id,
                    post_id=post_id)

        except ReactionDoesNotExists:
            self.reaction_storage.create_reaction_to_post(
                user_id=user_id,
                post_id=post_id,
                reaction_type=reaction_type)
            return

        is_undo_reaction = old_reaction_type == reaction_type
        if is_undo_reaction:
            self.reaction_storage.undo_post_reaction(user_id=user_id,
                                                     post_id=post_id)
        else:
            self.reaction_storage.update_post_reaction(
                user_id=user_id,
                post_id=post_id,
                reaction_type=reaction_type)
