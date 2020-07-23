
from fb_post_v2.interactors.storages import ReactionStorageInterface

from fb_post_v2.interactors.presenters import PresenterInterface


class GetTotalReactionCountInteractor:

    def __init__(self, reaction_storage: ReactionStorageInterface,
                 presenter: PresenterInterface):
        self.reaction_storage = reaction_storage
        self.presenter = presenter

    def get_total_reaction_count(self):
        count_dict_dto = self.reaction_storage.get_total_reaction_count_dto()
        response = self.presenter.get_total_reaction_count_response(
            get_total_reaction_count_dto=count_dict_dto
        )
        return response