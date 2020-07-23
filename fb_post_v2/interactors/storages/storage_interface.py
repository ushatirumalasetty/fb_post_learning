from abc import ABC, abstractmethod

from typing import Dict,List, Optional

from fb_post_v2.constants import ReactionTypeEnum

from fb_post_v2.interactors.storages.dtos  import (
    PostReactionsDto, CommentRepliesDto, PostCompleteDetailsDto,
    ReactionMetricsDto, TotalReactionCountDto
)


class StorageInterface():

    @abstractmethod
    def create_post(self, user_id: int, post_content: str) ->int:
        pass
    
    @abstractmethod
    def create_comment(self, user_id: int, post_id: int,
                       comment_content: str) ->int:
        pass

    @abstractmethod
    def is_valid_post_id(self, post_id: int):
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
    def is_valid_user_id(self, user_id: int):
        pass

    @abstractmethod
    def is_post_created_by_user(self, user_id: int, post_id: int):
        pass

    @abstractmethod
    def delete_post(self, post_id: int):
        pass

    @abstractmethod
    def get_replies_for_comment_dto(
            self, comment_id: int) ->List[CommentRepliesDto]:  #ToDo return type need to mention -done
        pass

    @abstractmethod
    def validate_post_reaction_if_exists_get_reaction_type(
        self, user_id: int, post_id: int)->ReactionTypeEnum:
        pass

    @abstractmethod
    def validate_comment_reaction_if_exists_get_reaction_type(
        self, user_id: int, comment_id: int)->ReactionTypeEnum:
        pass

    @abstractmethod
    def create_reaction_to_post(
        self, user_id: int, post_id: int,
        reaction_type: ReactionTypeEnum
    ):
        pass

    @abstractmethod
    def undo_post_reaction(self, user_id: int, post_id: int):
        pass

    @abstractmethod
    def update_post_reaction(self, user_id: int, post_id: int,
                             reaction_type: ReactionTypeEnum):
        pass

    @abstractmethod
    def create_reaction_to_comment(self, user_id: int, comment_id: int,
                                    reaction_type: ReactionTypeEnum):
        pass

    @abstractmethod
    def undo_comment_reaction(self, user_id: int, comment_id: int):
        pass

    @abstractmethod
    def update_comment_reaction(self, user_id: int, comment_id: int,
                             reaction_type: ReactionTypeEnum):
        pass

    @abstractmethod
    def get_total_reaction_count_dto(self) ->TotalReactionCountDto:
        pass

    @abstractmethod
    def get_reaction_metrics_dto(self, post_id: int) ->List[ReactionMetricsDto]:
        pass

    @abstractmethod
    def get_posts_with_more_positive_reactions(self) ->List[Optional[int]]:
        pass

    @abstractmethod
    def get_posts_reacted_by_user(self, user_id:int) ->List[Optional[int]]:
        pass

    @abstractmethod
    def get_reactions_to_post_dto(self, post_id: int) ->List[PostReactionsDto]:
        pass

    @abstractmethod
    def get_post_dto(self, post_id: int) ->PostCompleteDetailsDto:
        pass

    @abstractmethod
    def get_user_posts_dto(self, user_id: int) ->List[PostCompleteDetailsDto]:# -done returning type
        pass