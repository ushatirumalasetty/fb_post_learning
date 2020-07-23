from fb_post_v2.interactors.storages import ReactionStorageInterface
from fb_post_v2.interactors.storages import CommentStorageInterface

from fb_post_v2.interactors.presenters import PresenterInterface

from fb_post_v2.constants import ReactionTypeEnum

from fb_post_v2.exceptions import ReactionDoesNotExists

class ReactToCommentInteractor:

    def __init__(self,
                 comment_storage: CommentStorageInterface,
                 reaction_storage: ReactionStorageInterface,
                 presenter: PresenterInterface):

        self.reaction_storage = reaction_storage
        self.comment_storage = comment_storage
        self.presenter = presenter

    def react_to_comment(self, user_id: int, comment_id: int,
                      reaction_type: ReactionTypeEnum):

        is_valid_comment_id = self.comment_storage.is_valid_comment_id(
            comment_id=comment_id
        )
        invalid_comment_id_given = not is_valid_comment_id

        if invalid_comment_id_given:
            self.presenter.raise_invalid_comment_id_exception()
            return

        try:
            old_reaction_type = self.reaction_storage. \
                validate_comment_reaction_if_exists_get_reaction_type(
                    user_id=user_id,
                    comment_id=comment_id
                )
        except ReactionDoesNotExists: # TODO valid Exception -done
            self.reaction_storage.create_reaction_to_comment(
                user_id=user_id, comment_id=comment_id,
                reaction_type=reaction_type)
            return

        is_undo_reaction = old_reaction_type == reaction_type
        if is_undo_reaction:
            self.reaction_storage.undo_comment_reaction(user_id=user_id,
                                                        comment_id=comment_id)
        else:
            self.reaction_storage.update_comment_reaction(
                user_id=user_id,
                comment_id=comment_id,
                reaction_type=reaction_type)
