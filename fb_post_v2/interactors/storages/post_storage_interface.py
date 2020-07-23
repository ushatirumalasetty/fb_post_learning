from abc import ABC, abstractmethod

from typing import List

from fb_post_v2.constants import ReactionTypeEnum

from fb_post_v2.interactors.storages.dtos  import (
     PostCompleteDetailsDto
)


class PostStorageInterface():

    @abstractmethod
    def create_post(self, user_id: int, post_content: str) ->int:
        pass

    @abstractmethod
    def is_valid_post_id(self, post_id: int):
        pass
    
    
    @abstractmethod
    def is_post_created_by_user(self, user_id: int, post_id: int):
        pass

    @abstractmethod
    def delete_post(self, post_id: int):
        pass


    @abstractmethod
    def get_post_dto(self, post_id: int) ->PostCompleteDetailsDto:
        pass

    @abstractmethod
    def get_user_posts_dto(self, user_id: int) ->List[PostCompleteDetailsDto]:# -done returning type
        pass

    @abstractmethod
    def get_post_extra_details_dtos_for_presenter(
        self, get_post_dto: PostCompleteDetailsDto):
            pass