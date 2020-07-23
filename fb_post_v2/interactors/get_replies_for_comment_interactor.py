from fb_post_v2.interactors.storages import CommentStorageInterface

from fb_post_v2.interactors.presenters import PresenterInterface

from typing import List

from fb_post_v2.interactors.storages.dtos import CommentRepliesDto


class GetRepliesForCommentInteractor:

    def __init__(self, comment_storage: CommentStorageInterface,
                 presenter: PresenterInterface):
        self.comment_storage = comment_storage
        self.presenter = presenter

    def get_replies_for_comment(self,
                                comment_id: int
                                ) ->List[CommentRepliesDto]:

        is_valid_comment_id = self.comment_storage.is_valid_comment_id(
            comment_id = comment_id
        )
        invalid_comment_id_given = not is_valid_comment_id
        if invalid_comment_id_given:
            self.presenter.raise_invalid_comment_id_exception()
            return

        list_of_replies_dict = self.comment_storage.get_replies_for_comment_dto(
            comment_id = comment_id
        )
        response = self.presenter.get_replies_for_comment_response(
            comment_reply_dtos = list_of_replies_dict
        )

        return response