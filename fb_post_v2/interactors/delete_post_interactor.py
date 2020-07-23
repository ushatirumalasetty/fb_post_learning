from fb_post_v2.interactors.storages import PostStorageInterface

from fb_post_v2.interactors.presenters import PresenterInterface


class DeletePostInteractor:

    def __init__(self,
                 post_storage: PostStorageInterface,
                 presenter: PresenterInterface):

        self.post_storage = post_storage
        self.presenter = presenter

    def delete_post(self, user_id: int, post_id: int):

        is_valid_post_id = self.post_storage.is_valid_post_id(post_id=post_id)
        invalid_post_id_given = not is_valid_post_id

        if invalid_post_id_given:
            self.presenter.raise_invalid_post_id_exception()
            return

        is_post_created_by_user = self.post_storage.is_post_created_by_user(
            user_id=user_id, post_id=post_id
        )
        is_invalid_user_to_delete_post = not is_post_created_by_user

        if is_invalid_user_to_delete_post:
            self.presenter.raise_user_cannot_delete_exception(
                user_id=user_id, post_id=post_id)
            return

        self.post_storage.delete_post(post_id=post_id)
        empty_response = self.presenter.get_delete_post_response()

        return empty_response

