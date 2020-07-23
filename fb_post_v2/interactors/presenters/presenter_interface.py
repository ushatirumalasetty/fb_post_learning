from abc import ABC
from abc import abstractmethod

from fb_post_v2.constants import ReactionTypeEnum

from typing import List, Dict, Optional

from fb_post_v2.interactors.storages.dtos import (
    PostReactionsDto, CommentRepliesDto, PostCompleteDetailsDto,
    ReactionMetricsDto, TotalReactionCountDto, PostWithCommentsCountDto,
    PostWithReactionDetailsDto, CommentWithReactionDetailsDto,
    CommentWithRepliesCountDto
)

class PresenterInterface():

    @abstractmethod
    def get_create_post_response(self, post_id: int):
        pass

    @abstractmethod
    def get_create_comment_response(self, comment_id: int):
        pass
    
    @abstractmethod
    def raise_invalid_post_id_exception(self):
        pass
    
    @abstractmethod
    def get_reply_to_comment_response(self, comment_id: int):
        pass

    @abstractmethod
    def raise_invalid_comment_id_exception(self):
        pass

    @abstractmethod
    def raise_invalid_user_id_exception(self, user_id: int):
        pass

    @abstractmethod
    def raise_user_cannot_delete_exception(self, user_id: int, post_id: int):
        pass

    @abstractmethod
    def get_delete_post_response(self):
        pass

    @abstractmethod
    def get_replies_for_comment_response(
        self, comment_reply_dtos: List[CommentRepliesDto]
        ) ->List[CommentRepliesDto]:# ToDo dataclass at repliesdto--done
        pass

    @abstractmethod
    def get_total_reaction_count_response(
        self, get_total_reaction_count_dto: TotalReactionCountDto
    ): 
        pass

    @abstractmethod
    def get_reaction_metrics_response(
        self, get_reaction_metrics_dto: List[ReactionMetricsDto]):
        pass

    @abstractmethod
    def get_posts_with_more_positive_reactions_response(
        self, post_ids_list: List[Optional[int]]) ->List[Optional[int]]:
        pass

    @abstractmethod
    def get_posts_reacted_by_user_response(
        self, post_ids_list: List[Optional[int]]
    ) ->List[Optional[int]]:
        pass

    @abstractmethod
    def get_reactions_to_post_response(
        self, get_post_reaction_dto: List[PostReactionsDto]
    ) ->List[PostReactionsDto]:
        pass

    @abstractmethod
    def get_post_response(
        self,
        get_post_dto: PostCompleteDetailsDto,
        post_comment_count_dtos_list: List[PostWithCommentsCountDto],
        post_reactions_details_dto_list: List[PostWithReactionDetailsDto],
        comment_replies_count_dto_list: List[CommentWithRepliesCountDto],
        comment_reactions_details_dto_list: List[CommentWithReactionDetailsDto]
    ):# --done  Need to change dict to dto class
        pass


    @abstractmethod
    def get_user_posts_response(
        self,
        get_user_posts_dto: List[PostCompleteDetailsDto],
        post_comment_count_dtos_list: List[PostWithCommentsCountDto],
        post_reactions_details_dto_list: List[PostWithReactionDetailsDto],
        comment_replies_count_dto_list: List[CommentWithRepliesCountDto],
        comment_reactions_details_dto_list: List[CommentWithReactionDetailsDto]
    ):
        pass