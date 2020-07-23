import pytest


from fb_post_v2.interactors.storages.dtos import (
    UserDto, CommentDto, CommentRepliesDto, ReactionDto, PostDto,
    ReactionMetricsDto, TotalReactionCountDto, PostWithReactionDetailsDto
    
    )

from fb_post_v2.constants import ReactionTypeEnum
import datetime


@pytest.fixture
def user_dto():
    user_obj_dto = UserDto(
        user_id=1,
        name='anjali ameer',
        profile_pic='www.google.com'
        )
    return user_obj_dto


@pytest.fixture
def user_dtos():
    user_dtos = [
        UserDto(user_id=1,
                name='anjali ameer',
                profile_pic='www.google.com'),
        UserDto(user_id=2,
                name='che',
                profile_pic='')
    ]
    return user_dtos


@pytest.fixture
def  comment_dto():
    comment_obj_dto = CommentDto(
        comment_id=1,
        commented_by_id=1,
        post_id=1,
        commented_at=datetime.datetime(2019, 5, 19, 0, 0),
        content='Thanks.......',
        parent_comment_id=None
        )
    return comment_obj_dto


@pytest.fixture
def  comment_dtos():
    comment_dtos = [
        CommentDto(comment_id=1,
                   commented_by_id=1,
                   post_id=1,
                   commented_at=datetime.datetime(2019, 5, 19, 0, 0),
                   content='Thanks.......',
                   parent_comment_id=None),
        CommentDto(comment_id=2,
                   commented_by_id=2,
                   post_id=1,
                   commented_at=datetime.datetime(2019, 5, 19, 0, 0),
                   content='Thanks.......',
                   parent_comment_id=1)
    ]
    return comment_dtos


@pytest.fixture
def reaction_dtos():
    reaction_dtos = [
        ReactionDto(reaction_id=1,
                    reacted_by_id=1,
                    post_id=1,
                    reacted_at=datetime.datetime(2019, 5, 19, 0, 0),
                    reaction=ReactionTypeEnum.WOW.value,
                    comment_id=None),
        ReactionDto(reaction_id=2,
                    reacted_by_id=2,
                    comment_id=2,
                    reacted_at=datetime.datetime(2019, 5, 20, 0, 0),
                    reaction=ReactionTypeEnum.LOVE.value,
                    post_id=None)
    ]
    return reaction_dtos


@pytest.fixture
def post_dto():
    post_dto = PostDto(post_id=1,
                       posted_by_id=1,
                       posted_at=datetime.datetime(2019, 5, 20, 0, 0),
                       content='NEW POST')
    return post_dto


@pytest.fixture
def post_dtos():
    post_dtos = [
        PostDto(post_id=1,
                posted_by_id=1,
                posted_at=datetime.datetime(2019, 5, 20, 0, 0),
                content='NEW POST')
    ]
    return post_dtos

@pytest.fixture
def create_user_posts_dtos():
    post_dtos = [
        PostDto(post_id=1,
                posted_by_id=1,
                posted_at=datetime.datetime(2019, 5, 20, 0, 0),
                content='NEW POST1'),
        PostDto(post_id=2,
                posted_by_id=2,
                posted_at=datetime.datetime(2019, 5, 20, 0, 0),
                content='NEW POST2'),
                
    ]
    return post_dtos

 
@pytest.fixture
def comment_replies_dto():
    comment_replies_obj_dto = CommentRepliesDto(
        users_dto=[user_dto, user_dto],
        comments_dto=[comment_dto, comment_dto]
        )
    return comment_replies_obj_dto


@pytest.fixture
def reactions_metrics_dtos():
    reactions_metrics_dtos = [
        ReactionMetricsDto(reaction_type=ReactionTypeEnum.LOVE.value,
                           count=100
                           ),
        ReactionMetricsDto(reaction_type=ReactionTypeEnum.HAHA.value,
                           count=1000
                           ),
        ReactionMetricsDto(reaction_type=ReactionTypeEnum.WOW.value,
                           count=10000
                           )
    ]
    return reactions_metrics_dtos

@pytest.fixture
def get_total_reaction_count_dto():
    count_dto = TotalReactionCountDto(
        count=10
    )
    return count_dto
        
@pytest.fixture()
def post_reactions_dtos_with_duplicates():
    reaction_dtos = [
        ReactionDto(reaction_id=1,
                    reacted_by_id=1,
                    post_id=1,
                    reacted_at=datetime.datetime(2019, 5, 19, 0, 0),
                    reaction=ReactionTypeEnum.WOW.value,
                    comment_id=None),
        ReactionDto(reaction_id=2,
                    reacted_by_id=2,
                    comment_id=None,
                    reacted_at=datetime.datetime(2019, 5, 20, 0, 0),
                    reaction=ReactionTypeEnum.WOW.value,
                    post_id=1),
        ReactionDto(reaction_id=2,
                    reacted_by_id= 1,
                    comment_id=None,
                    reacted_at=datetime.datetime(2019, 5, 20, 0, 0),
                    reaction=ReactionTypeEnum.LOVE.value,
                    post_id=1),
        ReactionDto(reaction_id=2,
                    reacted_by_id=2,
                    comment_id=None,
                    reacted_at=datetime.datetime(2019, 5, 20, 0, 0),
                    reaction=ReactionTypeEnum.LIT.value,
                    post_id=1)
    ]
    return reaction_dtos




@pytest.fixture()
def comment_reactions_dtos_with_duplicates():
    reaction_dtos = [
        ReactionDto(reaction_id=1,
                    reacted_by_id=1,
                    post_id=None,
                    reacted_at=datetime.datetime(2019, 5, 19, 0, 0),
                    reaction=ReactionTypeEnum.WOW.value,
                    comment_id=1),
        ReactionDto(reaction_id=2,
                    reacted_by_id=2,
                    comment_id=1,
                    reacted_at=datetime.datetime(2019, 5, 20, 0, 0),
                    reaction=ReactionTypeEnum.WOW.value,
                    post_id=None),
        ReactionDto(reaction_id=2,
                    reacted_by_id=2,
                    comment_id=1,
                    reacted_at=datetime.datetime(2019, 5, 20, 0, 0),
                    reaction=ReactionTypeEnum.LOVE.value,
                    post_id=None),
        ReactionDto(reaction_id=2,
                    reacted_by_id=2,
                    comment_id=1,
                    reacted_at=datetime.datetime(2019, 5, 20, 0, 0),
                    reaction=ReactionTypeEnum.LIT.value,
                    post_id=None)
    ]
    return reaction_dtos


@pytest.fixture
def empty_post_reactions_details_dto():
    post_empty_dto_obj_list = [PostWithReactionDetailsDto(post_id=1,
                                                          reaction_type=[],
                                                          count=0)]
    return post_empty_dto_obj_list

@pytest.fixture
def get_total_reaction_count_dto_response():
    count_dto_response = {
        "count": 100
    }
    return count_dto_response


@pytest.fixture()
def get_reactions_metrics_dto_response():
    reaction_metrics_list = {
        "WOW":10000,
        "LOVE":100000,
        "LIT":100
    }
    return reaction_metrics_list


@pytest.fixture()
def get_post_reactions_dto_response():
    get_post_reactions_dto_response= [
            {
                "user_id": 1,
                "name": "iB Cricket",
                "profile_pic": "",
                "reaction": "LIKE"
            }
    ]
    return get_post_reactions_dto_response



@pytest.fixture()
def get_post_response():
    get_post_response = {
        'content': 'NEW POST',
        'post_id': 1,
        'posted_at': '13-12-2019,00:00:1568140200.00',
        'posted_by': {
            'name': 'James',
            'profile_pic': '',
            'user_id': 1
        },
        'reactions': {
            'count': 1,
            'type': [
                'HAHA'
            ]
        },
        'comments': [
            {
                'comment_content': 'nice post',
                'comment_id': 1,
                'commented_at': '13-12-2019,00:00:1568140200.00',
                'commenter': {
                    'name': 'James',
                    'profile_pic': '',
                    'user_id': 2
                },
                'reactions': {
                    'count': 1,
                    'type': [
                        'SAD'
                    ]
                },
                'replies': [
                    {
                        'comment_content': 'nice post',
                        'comment_id': 2,
                        'commented_at': '13-12-2019,00:00:1568140200.00',
                        'commenter': {
                            'name': 'James',
                            'profile_pic': '',
                            'user_id': 2
                        }
                    },
                    {
                        'count': 1,
                        'type': [
                            'WOW'
                        ]
                    }
                ],
                'replies_count': 1
            }

        ],
        "comments_count": 1
    }
    return get_post_response


@pytest.fixture()
def get_user_posts_response():
    get_user_posts_response = {
        'post_content': 'NEW POST',
        'post_id': 1,
        'posted_at': '13-12-2019,00:00:1568140200.00',
        'posted_by': {
            'name': 'James',
            'profile_pic': '',
            'user_id': 1
        },
        'reactions': {
            'count': 1,
            'type': [
                'HAHA'
            ]
        },
        'comments': [
            {
                'comment_content': 'nice post',
                'comment_id': 1,
                'commented_at': '13-12-2019,00:00:1568140200.00',
                'commenter': {
                    'name': 'James',
                    'profile_pic': '',
                    'user_id': 2
                },
                'reactions': {
                    'count': 1,
                    'type': [
                        'SAD'
                    ]
                },
                'replies': [
                    {
                        'comment_content': 'nice post',
                        'comment_id': 2,
                        'commented_at': '13-12-2019,00:00:1568140200.00',
                        'commenter': {
                            'name': 'James',
                            'profile_pic': '',
                            'user_id': 2
                        }
                    },
                    {
                        'count': 1,
                        'type': [
                            'WOW'
                        ]
                    }
                ],
                'replies_count': 1
            }

        ],
        "comments_count": 1
    }
    return get_user_posts_response
