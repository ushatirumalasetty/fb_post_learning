from fb_post_v2.interactors.storages import ReactionStorageInterface
from fb_post_v2.interactors.storages import PostStorageInterface

from fb_post_v2.interactors.presenters import PresenterInterface


class GetReactionsToPostInteractor:

    def __init__(self,
                 post_storage: PostStorageInterface,
                 reaction_storage: ReactionStorageInterface,
                 presenter: PresenterInterface):
        self.post_storage = post_storage
        self.reaction_storage = reaction_storage
        self.presenter = presenter

    def get_reactions_to_post(self, post_id: int):

        is_valid_post_id = self.post_storage.is_valid_post_id(post_id=post_id)
        invalid_post_id_given = not is_valid_post_id

        if invalid_post_id_given:
            self.presenter.raise_invalid_post_id_exception()
            return

        get_post_reaction_dto = self.reaction_storage.get_reactions_to_post_dto(
            post_id=post_id
        )
        response = self.presenter.get_reactions_to_post_response(
            get_post_reaction_dto=get_post_reaction_dto
        )

        return response
