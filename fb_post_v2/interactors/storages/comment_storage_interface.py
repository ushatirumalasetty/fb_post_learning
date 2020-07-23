from abc import ABC, abstractmethod

from typing import List

from fb_post_v2.constants import ReactionTypeEnum

from fb_post_v2.interactors.storages.dtos  import (
    CommentRepliesDto
)


class CommentStorageInterface():

    @abstractmethod
    def create_comment(self, user_id: int, post_id: int,
                       comment_content: str) ->int:
        pass

    
    @abstractmethod
    def is_valid_comment_id(self, comment_id):
        pass
    
    @abstractmethod
    def reply_to_comment(self, user_id: int,
                         comment_id: int,
                         reply_content: str) ->int:
        pass

    @abstractmethod
    def return_comment_id_if_is_comment_id_or_return_parent_comment_id(
        self, comment_id: int) ->int:
        pass


    @abstractmethod
    def get_replies_for_comment_dto(
            self, comment_id: int) ->List[CommentRepliesDto]:  #ToDo return type need to mention -done
        pass


    