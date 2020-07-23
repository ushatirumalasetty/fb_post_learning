from datetime import datetime

from dataclasses import dataclass

from fb_post_v2.constants import ReactionTypeEnum

from typing import List, Optional



@dataclass()
class UserDto:
    user_id: int
    name: str
    profile_pic: str


@dataclass()
class PostReactionsDto:
    user_dto: UserDto
    reaction: ReactionTypeEnum


@dataclass()
class CommentDto:
    comment_id: int
    commented_by_id: int
    post_id: Optional[int]
    commented_at: datetime
    content: str
    parent_comment_id: Optional

@dataclass()
class ReactionDto:
    reaction_id: int
    reacted_by_id: int
    post_id: Optional[int]
    comment_id: Optional[int]
    reacted_at: datetime
    reaction: ReactionTypeEnum
    
@dataclass()
class PostDto:
    post_id: int
    posted_by_id: int
    posted_at: datetime
    content: str


@dataclass()
class PostCompleteDetailsDto:
    post_dto: PostDto
    user_dtos: List[UserDto]
    comment_dtos: List[CommentDto]
    reaction_dtos: List[ReactionDto]

@dataclass()
class CommentRepliesDto:
    users_dto: List[UserDto]
    comments_dto: List[CommentDto]


@dataclass()
class ReactionMetricsDto:
    reaction_type: ReactionTypeEnum
    count: int

@dataclass()
class TotalReactionCountDto:
    count: int


@dataclass
class CommentWithRepliesCountDto:
    comment_id: int
    replies_count: int

@dataclass
class PostWithCommentsCountDto:
    post_id: int
    comments_count: int


@dataclass
class CommentWithReactionDetailsDto:
    comment_id: int
    reaction_type: List[ReactionTypeEnum]
    count: int

@dataclass
class PostWithReactionDetailsDto:
    post_id: int
    reaction_type: List[ReactionTypeEnum]
    count: int










""""
@dataclass()
class UserDto:
    user_id: int
    name: str
    profile_pic: str
    username: str


@dataclass()
class ReactionDto:
    reaction_id: int
    comment_id: Optional[int]
    post_id: Optional[int]
    user_id: int
    reaction_type: ReactionType


@dataclass()
class PostReactionCompleteDetailsDto:
    user_dtos: List[UserDto]
    reaction_dtos: List[ReactionDto]


@dataclass()
class CommentDto:
    comment_id: int
    user_id: int
    post_id: Optional[int]
    comment_content: str
    pub_date_time: datetime
    parent_comment: Optional


@dataclass()
class CommentRepliesDto:
    users_dto: List[UserDto]
    comments_dto: List[CommentDto]


@dataclass()
class PostDto:
    user_id: int
    post_content: str
    post_id: int
    pub_date_time: datetime


@dataclass()
class PostCompleteDetailsDto:
    post_dto: PostDto
    users_dto: List[UserDto]
    comments_dto: List[CommentDto]
    reactions_dto: List[ReactionDto]
"""