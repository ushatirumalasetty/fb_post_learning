from fb_post_v2.interactors.storages import CommentStorageInterface
from fb_post_v2.interactors.storages import PostStorageInterface

from fb_post_v2.interactors.presenters import PresenterInterface


class CreateCommentInteractor:

    def __init__(self,
                 post_storage: PostStorageInterface,
                 comment_storage: CommentStorageInterface,
                 presenter: PresenterInterface):

        self.post_storage = post_storage
        self.comment_storage = comment_storage
        self.presenter = presenter

    def create_comment(self, user_id: int, post_id: int,
                       comment_content: str) ->int:

        is_valid_post_id = self.post_storage.is_valid_post_id(post_id=post_id)
        invalid_post_id_given = not is_valid_post_id

        if invalid_post_id_given:
            self.presenter.raise_invalid_post_id_exception()
            return

        new_comment_id = self.comment_storage.create_comment(
            user_id=user_id,
            post_id=post_id,
            comment_content=comment_content
        )
        response = self.presenter.get_create_comment_response(
            comment_id=new_comment_id
            )
        return response
