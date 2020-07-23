from fb_post_v2.interactors.storages import ReactionStorageInterface

from fb_post_v2.interactors.presenters import PresenterInterface

from typing import List, Optional

class GetPostsWithMorePositiveReactionsInteractor:

    def __init__(self, reaction_storage: ReactionStorageInterface,
                 presenter: PresenterInterface):
        self.reaction_storage = reaction_storage
        self.presenter = presenter

    def get_posts_with_more_positive_reactions(self) ->List[Optional[int]]:

        post_ids_list = \
            self.reaction_storage.get_posts_with_more_positive_reactions()
        response = self.presenter. \
            get_posts_with_more_positive_reactions_response(
                post_ids_list=post_ids_list
            )
        return response