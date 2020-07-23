from fb_post_v2.interactors.storages import ReactionStorageInterface
from fb_post_v2.interactors.storages import PostStorageInterface


from fb_post_v2.interactors.presenters import PresenterInterface


class GetReactionMetricsInteractor:

    def __init__(self, reaction_storage: ReactionStorageInterface,
                 post_storage: PostStorageInterface,
                 presenter: PresenterInterface):

        self.reaction_storage = reaction_storage
        self.post_storage = post_storage
        self.presenter = presenter

    def get_reaction_metrics(self, post_id: int):

        is_valid_post_id = self.post_storage.is_valid_post_id(post_id=post_id)
        invalid_post_id_given = not is_valid_post_id

        if invalid_post_id_given:
            self.presenter.raise_invalid_post_id_exception()
            return

        reaction_metrics_dto = self.reaction_storage.get_reaction_metrics_dto(
            post_id=post_id
        )
        response = self.presenter.get_reaction_metrics_response(
            get_reaction_metrics_dto=reaction_metrics_dto
        )
        
        return response