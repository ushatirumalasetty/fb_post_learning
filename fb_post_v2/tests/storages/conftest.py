
import datetime

import pytest

from freezegun import freeze_time

from fb_post_v2.models import Post, User, Comment, Reaction

from fb_post_v2.constants import ReactionTypeEnum

from fb_post_v2.interactors.storages.dtos import (
    PostDto, UserDto, CommentDto, ReactionDto
)

@pytest.fixture()
@freeze_time("2020-10-10")
def create_users():
    users = [
        {
            "name": "che",
            "profile_pic": "che/profile_pic",
            "username": "che123"
        },
        {
            "name": "stevejobs",
            "profile_pic": "stevjobs/profile_pic",
            "username": "steve123"
        }
    ]
    User.objects.bulk_create(
        [
            User(name=user['name'],
                 profile_pic=user["profile_pic"],
                 username=user["username"]) 
                for user in users
        ]
    )

@pytest.fixture()
@freeze_time("2020-10-10")
def create_posts():
    posts = [
        {
            "posted_by_id": 1,
            "post_content": "New Post1"
        },
        {
            "posted_by_id": 2,
            "post_content": "New Post2"
        },
    ]
    Post.objects.bulk_create(
        [
            Post(posted_by_id=post['posted_by_id'],
                 content=post["post_content"])
                for post in posts
        ]
    )

@pytest.fixture()
@freeze_time("2020-10-10")
def create_comments():
    comments = [
        {
            "commented_by_id": 1,
            "post_id": 1,
            "comment_content": "New Comment1",
            "parent_comment_id": None
        },
        {
            "commented_by_id": 1,
            "post_id": 2,
            "comment_content": "New Comment2",
            "parent_comment_id": 1
        }
    ]
    Comment.objects.bulk_create(
        [
            Comment(commented_by_id=comment["commented_by_id"],
                    post_id=comment["post_id"],
                    content=comment["comment_content"],
                    parent_comment_id=comment["parent_comment_id"])
            for comment in comments
            ]
        )




@pytest.fixture()
@freeze_time("2020-10-10")
def get_post_create_comments():
    comments = [
        {
            "commented_by_id": 1,
            "post_id": 1,
            "comment_content": "New Comment1",
            "parent_comment_id": None
        },
        {
            "commented_by_id": 2,
            "post_id": 1,
            "comment_content": "New Comment2",
            "parent_comment_id": 1
        }
    ]
    Comment.objects.bulk_create(
        [
            Comment(commented_by_id=comment["commented_by_id"],
                    post_id=comment["post_id"],
                    content=comment["comment_content"],
                    parent_comment_id=comment["parent_comment_id"])
            for comment in comments
            ]
        )


@pytest.fixture()
@freeze_time("2020-10-10")
def create_reactions():
    reactions = [
        {
            "reacted_by_id": 1,
            "post_id": 1,
            "comment_id": None,
            "reaction": ReactionTypeEnum.WOW.value,
        },
        {
            "reacted_by_id": 1,
            "post_id": None,
            "comment_id": 1,
            "reaction": ReactionTypeEnum.LOVE.value,
        }
    ]
    Reaction.objects.bulk_create(
        [
            Reaction(reacted_by_id=reaction["reacted_by_id"],
                     post_id=reaction["post_id"],
                     comment_id=reaction["comment_id"],
                     reaction=reaction["reaction"])
                for reaction in reactions
            ]
    )

@pytest.fixture()
@freeze_time("2020-10-10")
def create_post_reactions():
    reactions = [
        {
            "reacted_by_id": 1,
            "post_id": 1,
            "comment_id": None,
            "reaction": ReactionTypeEnum.WOW.value,
        },
        {
            "reacted_by_id": 2,
            "post_id": 1,
            "comment_id": None,
            "reaction": ReactionTypeEnum.LOVE.value,
        }
    ]
    Reaction.objects.bulk_create(
        [
            Reaction(reacted_by_id=reaction["reacted_by_id"],
                     post_id=reaction["post_id"],
                     comment_id=reaction["comment_id"],
                     reaction=reaction["reaction"])
                for reaction in reactions
            ]
    )


@pytest.fixture
def get_post_user_dtos():
    user_dtos = [
        UserDto(user_id=1,
                name='che',
                profile_pic='che/profile_pic'),
        UserDto(user_id=2,
                name='stevejobs',
                profile_pic='stevjobs/profile_pic')
    ]
    return user_dtos

@pytest.fixture
def  get_post_comment_dtos():
    comment_obj_dto = [
        CommentDto(comment_id=1,
                   commented_by_id=1,
                   post_id=1,
                   commented_at=datetime.datetime(2020, 10, 10, 0, 0),
                   content='New Comment1',
                   parent_comment_id=None),
        CommentDto(comment_id=2,
                   commented_by_id=2,
                   post_id=1,
                   commented_at=datetime.datetime(2020, 10, 10, 0, 0),
                   content='New Comment2',
                   parent_comment_id=1)
    ]
    return comment_obj_dto

@pytest.fixture
def get_post_reaction_dtos():
    reaction_dtos = [
        ReactionDto(reaction_id=1,
                    reacted_by_id=1,
                    post_id=1,
                    reacted_at=datetime.datetime(2020, 10, 10, 0, 0),
                    reaction=ReactionTypeEnum.WOW.value,
                    comment_id=None),
        ReactionDto(reaction_id=2,
                    reacted_by_id=1,
                    comment_id=1,
                    reacted_at=datetime.datetime(2020, 10, 10, 0, 0),
                    reaction=ReactionTypeEnum.LOVE.value,
                    post_id=None)
    ]
    return reaction_dtos

@pytest.fixture
def get_post_post_dto():
    post_dto = PostDto(post_id=1,
                       posted_by_id=1,
                       posted_at=datetime.datetime(2020, 10, 10, 0, 0),
                       content='New Post1')
    return post_dto
