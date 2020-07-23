from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface


class GetTotalReactionsCountInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_total_reactions_count(self, presenter=PresenterInterface):
        reactions_count_dict = self.storage.get_total_reactions_count()
        return presenter.get_total_reactions_count_response(
            reactions_count_dict
            )
