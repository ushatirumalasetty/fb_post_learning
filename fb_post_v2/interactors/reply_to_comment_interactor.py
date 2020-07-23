from fb_post_v2.interactors.storages import CommentStorageInterface

from fb_post_v2.interactors.presenters import PresenterInterface


class ReplyToCommentInteractor:

    def __init__(self, comment_storage:CommentStorageInterface,
                 presenter: PresenterInterface):

        self.comment_storage = comment_storage
        self.presenter = presenter

    def reply_to_comment(self,
                         user_id: int,
                         comment_id: int,
                         reply_content: str):

        is_valid_comment_id = self.comment_storage.is_valid_comment_id(
            comment_id=comment_id)
        invalid_comment_id_given = not is_valid_comment_id

        if invalid_comment_id_given:
            self.presenter.raise_invalid_comment_id_exception()
            return

        comment_id = \
            self.comment_storage.\
                return_comment_id_if_is_comment_id_or_return_parent_comment_id(
            comment_id=comment_id
        )

        new_comment_id = self.comment_storage.reply_to_comment(
            user_id=user_id,
            comment_id=comment_id,
            reply_content=reply_content
        )

        response = self.presenter.get_reply_to_comment_response(
            comment_id=new_comment_id)
        return response
