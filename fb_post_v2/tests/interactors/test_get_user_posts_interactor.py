import datetime

from unittest.mock import create_autospec, patch

from fb_post_v2.interactors.storages import PostStorageInterface

from fb_post_v2.interactors.presenters import PresenterInterface

from fb_post_v2.interactors.get_user_posts_interactor import \
    GetUserPostsInteractor

from fb_post_v2.interactors.storages.dtos import (
    PostCompleteDetailsDto, PostWithCommentsCountDto,
    PostWithReactionDetailsDto, CommentWithRepliesCountDto,
    CommentWithReactionDetailsDto, CommentDto
)


class TestGetUserPostsInteractor:

    @patch.object(GetUserPostsInteractor,
                  'get_user_posts_extra_dto_details_for_presenter')
    def test_get_user_posts_interactor_(self,
                                        user_dtos,
                                        post_dto,
                                        comment_dtos,
                                        reaction_dtos,
                                        get_user_posts_response):

        # Arrange
        user_id = 1
        expected_post_details_list_mock = get_user_posts_response

        post_storage = create_autospec(PostStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetUserPostsInteractor(post_storage=post_storage,
                                            presenter=presenter)
        
        post_comment_count_dtos_list = [],
        post_reactions_details_dto_list = [],
        comment_replies_count_dto_list = [],
        comment_reactions_details_dto_list = []

        empty_lists = (post_comment_count_dtos_list,
                      post_reactions_details_dto_list,
                      comment_replies_count_dto_list,
                      comment_reactions_details_dto_list)

        interactor.get_user_posts_extra_dto_details_for_presenter.return_value = \
            empty_lists
    
        get_user_posts_dtos = [
            PostCompleteDetailsDto(post_dto=post_dto,
                                   user_dtos=user_dtos,
                                   comment_dtos=comment_dtos,
                                   reaction_dtos=reaction_dtos)
        ]
        
        post_storage.get_user_posts_dto.return_value = get_user_posts_dtos
        presenter.get_user_posts_response.return_value = \
            expected_post_details_list_mock
        
        # Act
        actual_post_details_list = interactor.get_user_posts(user_id=user_id)

        # Assert
        assert actual_post_details_list == expected_post_details_list_mock
        post_storage.get_user_posts_dto.assert_called_once_with(
            user_id=user_id
        )

        presenter.get_user_posts_response.assert_called_once_with(
            get_user_posts_dto=get_user_posts_dtos,
            post_comment_count_dtos_list=post_comment_count_dtos_list,
            post_reactions_details_dto_list=post_reactions_details_dto_list,
            comment_replies_count_dto_list=comment_replies_count_dto_list,
            comment_reactions_details_dto_list= \
                comment_reactions_details_dto_list
        )



    
    def test_get_user_posts_extra_dto_details_for_presenter(self,
                                                       user_dtos,
                                                       post_dto,
                                                       comment_dtos,
                                                       reaction_dtos):

        # Arrange
        post_id = 1

        post_storage = create_autospec(PostStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetUserPostsInteractor(post_storage=post_storage,
                                       presenter=presenter)

        exp_post_comment_count_dtos_list = [
            PostWithCommentsCountDto(post_id=1, comments_count=1)]

        exp_post_reactions_details_dto_list = [
            PostWithReactionDetailsDto(post_id=1,
                                       reaction_type=["WOW"],
                                       count=1)]

        exp_comment_replies_count_dto_list = [
            CommentWithRepliesCountDto(comment_id=1,
                                       replies_count=1)]

        exp_comment_reactions_details_dto_list = [
            CommentWithReactionDetailsDto(comment_id=1,
                                          reaction_type=[],
                                          count=0),
            CommentWithReactionDetailsDto(comment_id=2,
                                          reaction_type=["LOVE"],
                                          count=1)]

        get_user_posts_dto = [PostCompleteDetailsDto(user_dtos=user_dtos,
                                              post_dto=post_dto,
                                              comment_dtos=comment_dtos,
                                              reaction_dtos=reaction_dtos)]

        # Act
        (post_comment_count_dtos_list, post_reactions_details_dto_list,
        comment_replies_count_dto_list, comment_reactions_details_dto_list) = \
            interactor.get_user_posts_extra_dto_details_for_presenter(
                post_dtos_list=get_user_posts_dto)

        # Assert
        assert post_comment_count_dtos_list == \
             exp_post_comment_count_dtos_list
        assert post_reactions_details_dto_list == \
             exp_post_reactions_details_dto_list
        assert comment_replies_count_dto_list == \
            exp_comment_replies_count_dto_list
        assert comment_reactions_details_dto_list == \
            exp_comment_reactions_details_dto_list
    

    def test_get_user_posts_extra_dto_details_for_presenter_comment_with_no_replies(
        self,
        post_dto,
        reaction_dtos,
        user_dtos
    ):

        # Arrange
        comment1 = CommentDto(comment_id=1,
                             commented_by_id=1,
                             post_id=1,
                             commented_at = \
                                datetime.datetime(2020, 10, 10, 0, 0),
                             content='HII',
                             parent_comment_id=None)
        comment2 = CommentDto(comment_id=2,
                             commented_by_id=2,
                             post_id=2,
                             commented_at = \
                                datetime.datetime(2020, 10, 10, 0, 0) ,
                             content='HII',
                             parent_comment_id=None)
        testing_comment_dtos_list = [comment1, comment2]

        expected_comment_count_dtos = [
            CommentWithRepliesCountDto(comment_id=1, replies_count=0),
            CommentWithRepliesCountDto(comment_id=2, replies_count=0)
        ]
        post_complete_dto = [
            PostCompleteDetailsDto(user_dtos=user_dtos,
                                   post_dto=post_dto,
                                   comment_dtos= \
                                       testing_comment_dtos_list,
                                   reaction_dtos=reaction_dtos)
        ]

        post_storage = create_autospec(PostStorageInterface)
        presenter =  create_autospec(PresenterInterface)
        interactor = GetUserPostsInteractor(post_storage=post_storage,
                                       presenter=presenter)

        # Act
        (post_comment_count_dtos_list,
        post_reactions_details_dto_list,
        actual_comment_replies_count_dto_list,
        comment_reactions_details_dto_list) = interactor. \
            get_user_posts_extra_dto_details_for_presenter(post_complete_dto)

        # Assert
        assert actual_comment_replies_count_dto_list == \
            expected_comment_count_dtos


    def test_get_user_posts_extra_dto_details_for_presenter_with_comment_with_replies(
            self,
            post_dto
    ):

        # Arrange
        comment1 = CommentDto(comment_id=1,
                             commented_by_id=1,
                             post_id=1,
                             commented_at = \
                                datetime.datetime(2020, 10, 10, 0, 0),
                             content='HII',
                             parent_comment_id=None)
        comment2 = CommentDto(comment_id=2,
                             commented_by_id=2,
                             post_id=2,
                             commented_at = \
                                datetime.datetime(2020, 10, 10, 0, 0),
                             content='HII',
                             parent_comment_id=1)
        comment3 = CommentDto(comment_id=3,
                             commented_by_id=2,
                             post_id=2,
                             commented_at = \
                                datetime.datetime(2020, 10, 10, 0, 0),
                             content='HII',
                             parent_comment_id=None)
        comment4 = CommentDto(comment_id=3,
                             commented_by_id=2,
                             post_id=2,
                             commented_at = \
                                datetime.datetime(2020, 10, 10, 0, 0),
                             content='HII',
                             parent_comment_id=1)

        testing_comment_dtos_list = [comment1, comment2, comment3, comment4]

        expected_comment_count_dtos = [
            CommentWithRepliesCountDto(comment_id=1, replies_count=2),
            CommentWithRepliesCountDto(comment_id=3, replies_count=0)
        ]

        post_storage = create_autospec(PostStorageInterface)
        presenter =  create_autospec(PresenterInterface)
        interactor = GetUserPostsInteractor(post_storage=post_storage,
                                       presenter=presenter)

        post_complete_dto = [
            PostCompleteDetailsDto(user_dtos=[],
                                   post_dto=post_dto,
                                   comment_dtos= \
                                       testing_comment_dtos_list,
                                   reaction_dtos=[])
        ]

        
        # Act
        (post_comment_count_dtos_list,
        post_reactions_details_dto_list,
        actual_comment_replies_count_dto_list,
        comment_reactions_details_dto_list) = interactor. \
            get_user_posts_extra_dto_details_for_presenter(post_complete_dto)

        
        # Assert
        assert actual_comment_replies_count_dto_list == \
            expected_comment_count_dtos



    def test_get_user_posts_extra_dto_details_for_presenter_with_post_no_comments(
        self, post_dto
    ):

        # Arrrange
        expected_post_comment_count_dtos_list = [
            PostWithCommentsCountDto(post_id=1, comments_count=0)
            ]
        post_storage = create_autospec(PostStorageInterface)
        presenter =  create_autospec(PresenterInterface)
        interactor = GetUserPostsInteractor(post_storage=post_storage,
                                       presenter=presenter)

        post_complete_dto = [
            PostCompleteDetailsDto(user_dtos=[],
                                   post_dto=post_dto,
                                   comment_dtos= [],
                                   reaction_dtos=[])
        ]
                                                   

        # Act
        (actual_post_comment_count_dtos_list,
        post_reactions_details_dto_list,
        actual_comment_replies_count_dto_list,
        comment_reactions_details_dto_list) = interactor. \
            get_user_posts_extra_dto_details_for_presenter(post_complete_dto)

        # Assert
        assert actual_post_comment_count_dtos_list == \
            expected_post_comment_count_dtos_list


    def test_get_user_posts_extra_dto_details_for_presenter_with_post_with_comments(
        self, post_dto
    ):

        # Arrrange
        expected_post_comment_count_dtos_list = [
            PostWithCommentsCountDto(post_id=1, comments_count=2)
            ]
        comment1 = CommentDto(comment_id=1,
                             commented_by_id=1,
                             post_id=1,
                             commented_at = \
                                datetime.datetime(2020, 10, 10, 0, 0),
                             content='HII',
                             parent_comment_id=None)
        comment2 = CommentDto(comment_id=2,
                             commented_by_id=2,
                             post_id=1,
                             commented_at = \
                                datetime.datetime(2020, 10, 10, 0, 0),
                             content='HII',
                             parent_comment_id=1)
        comment3 = CommentDto(comment_id=3,
                             commented_by_id=2,
                             post_id=1,
                             commented_at = \
                                datetime.datetime(2020, 10, 10, 0, 0),
                             content='HII',
                             parent_comment_id=None)
        comments_dtos_list = [comment1, comment2, comment3]
        post_storage = create_autospec(PostStorageInterface)
        presenter =  create_autospec(PresenterInterface)
        interactor = GetUserPostsInteractor(post_storage=post_storage,
                                       presenter=presenter)

        post_complete_dto = [
            PostCompleteDetailsDto(user_dtos=[],
                                   post_dto=post_dto,
                                   comment_dtos= \
                                       comments_dtos_list,
                                   reaction_dtos=[])
        ]

        # Act
        (actual_post_comment_count_dtos_list,
        post_reactions_details_dto_list,
        actual_comment_replies_count_dto_list,
        comment_reactions_details_dto_list) = interactor. \
            get_user_posts_extra_dto_details_for_presenter(post_complete_dto)

        # Assert
        assert actual_post_comment_count_dtos_list == \
            expected_post_comment_count_dtos_list


    def test_get_user_posts_extra_dto_details_for_presenter_with_post_with_reactions(
        self, post_dto, user_dtos, comment_dtos,
        post_reactions_dtos_with_duplicates
    ):

        # Arrrange
        expected_post_comment_count_dtos_list = [
            PostWithReactionDetailsDto(post_id=1,
                                       reaction_type=["LIT", "LOVE", "WOW"],
                                       count=4)
            ]
        post_storage = create_autospec(PostStorageInterface)
        presenter =  create_autospec(PresenterInterface)
        interactor = GetUserPostsInteractor(post_storage=post_storage,
                                       presenter=presenter)

        post_complete_dto = [
            PostCompleteDetailsDto(user_dtos=user_dtos,
                                   post_dto=post_dto,
                                   comment_dtos=comment_dtos,
                                   reaction_dtos= \
                                       post_reactions_dtos_with_duplicates)
        ]

        # Act
        (post_comment_count_dtos_list,
        actual_post_reactions_details_dto_list,
        comment_replies_count_dto_list,
        comment_reactions_details_dto_list) = interactor. \
            get_user_posts_extra_dto_details_for_presenter(post_complete_dto)

        # Assert
        assert actual_post_reactions_details_dto_list == \
            expected_post_comment_count_dtos_list


    def test_get_user_posts_extra_dto_details_for_presenter_with_post_no_reactions(
        self, post_dto, user_dtos, comment_dtos
    ):

        # Arrrange
        expected_post_comment_count_dtos_list = [
            PostWithReactionDetailsDto(post_id=1, reaction_type=[], count=0)
            ]
        post_storage = create_autospec(PostStorageInterface)
        presenter =  create_autospec(PresenterInterface)
        interactor = GetUserPostsInteractor(post_storage=post_storage,
                                       presenter=presenter)

        post_complete_dto = [
            PostCompleteDetailsDto(user_dtos=user_dtos,
                                   post_dto=post_dto,
                                   comment_dtos=comment_dtos,
                                   reaction_dtos=[])
        ]

        # Act
        (post_comment_count_dtos_list,
        actual_post_reactions_details_dto_list,
        comment_replies_count_dto_list,
        comment_reactions_details_dto_list) = interactor. \
            get_user_posts_extra_dto_details_for_presenter(post_complete_dto)

        # Assert
        assert actual_post_reactions_details_dto_list == \
            expected_post_comment_count_dtos_list


    def test_get_user_posts_extra_dto_details_for_presenter_with_comment_with_reactions(
        self, post_dto, user_dtos, comment_dtos,
        comment_reactions_dtos_with_duplicates
    ):

        # Arrrange
        expected_comment_reactions_details_dto_list = [
            CommentWithReactionDetailsDto(comment_id=1,
                                          reaction_type=["LIT", "LOVE", "WOW"],
                                          count=4),
            CommentWithReactionDetailsDto(comment_id=2,
                                          reaction_type=[],
                                          count=0),
            ]
        post_storage = create_autospec(PostStorageInterface)
        presenter =  create_autospec(PresenterInterface)
        interactor = GetUserPostsInteractor(post_storage=post_storage,
                                       presenter=presenter)

        post_complete_dto = [
            PostCompleteDetailsDto(user_dtos=user_dtos,
                                   post_dto=post_dto,
                                   comment_dtos=comment_dtos,
                                   reaction_dtos= \
                                       comment_reactions_dtos_with_duplicates)
        ]

        # Act
        (post_comment_count_dtos_list,
        post_reactions_details_dto_list,
        comment_replies_count_dto_list,
        actual_comment_reactions_details_dto_list) = interactor. \
            get_user_posts_extra_dto_details_for_presenter(post_complete_dto)

        # Assert
        assert actual_comment_reactions_details_dto_list == \
            expected_comment_reactions_details_dto_list



    def test_get_user_posts_extra_dto_details_for_presenter_with_comment_with_no_reactions(
        self, post_dto, user_dtos,
        post_reactions_dtos_with_duplicates
    ):

        # Arrrange
        empty_comment_dtos = []
        expected_comment_reactions_details_dto_list = []
        post_storage = create_autospec(PostStorageInterface)
        presenter =  create_autospec(PresenterInterface)
        interactor = GetUserPostsInteractor(post_storage=post_storage,
                                       presenter=presenter)

        post_complete_dto = [
            PostCompleteDetailsDto(user_dtos=user_dtos,
                                   post_dto=post_dto,
                                   comment_dtos=empty_comment_dtos,
                                   reaction_dtos= \
                                       post_reactions_dtos_with_duplicates)
        ]

        # Act
        (post_comment_count_dtos_list,
        post_reactions_details_dto_list,
        comment_replies_count_dto_list,
        actual_comment_reactions_details_dto_list) = interactor. \
            get_user_posts_extra_dto_details_for_presenter(post_complete_dto)

        # Assert
        assert actual_comment_reactions_details_dto_list == \
            expected_comment_reactions_details_dto_list


    def test_get_user_posts_extra_dto_details_for_presenter_with_multiple_data(
            self,
            user_dtos,
            create_user_posts_dtos,
            post_reactions_dtos_with_duplicates,
            comment_reactions_dtos_with_duplicates,
            comment_dtos,
            reaction_dtos):

        # Arrange
        post_id = 1
        post_storage = create_autospec(PostStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetUserPostsInteractor(post_storage=post_storage,
                                       presenter=presenter)
        post_and_comments_reactions_dtos = \
            (post_reactions_dtos_with_duplicates
            + comment_reactions_dtos_with_duplicates)

        exp_post_comment_count_dtos_list = [
            PostWithCommentsCountDto(post_id=1, comments_count=1),
            PostWithCommentsCountDto(post_id=2, comments_count=0)
        ]

        exp_post_reactions_details_dto_list = [
            PostWithReactionDetailsDto(post_id=1,
                                       reaction_type=["LIT", "LOVE", "WOW"],
                                       count=4),
            PostWithReactionDetailsDto(post_id=2,
                                       reaction_type=[],
                                       count=0)]

        exp_comment_replies_count_dto_list = [
            CommentWithRepliesCountDto(comment_id=1,
                                       replies_count=1)]

        exp_comment_reactions_details_dto_list = [
            CommentWithReactionDetailsDto(comment_id=1,
                                          reaction_type=["LIT", "LOVE", "WOW"],
                                          count=4),
            CommentWithReactionDetailsDto(comment_id=2,
                                          reaction_type=[],
                                          count=0)]

        get_user_posts_dto = [
            PostCompleteDetailsDto(
                user_dtos=user_dtos,
                post_dto=create_user_posts_dtos[0],
                comment_dtos=comment_dtos,
                reaction_dtos=post_and_comments_reactions_dtos
            ),
            PostCompleteDetailsDto(
                user_dtos=[],
                post_dto=create_user_posts_dtos[1],
                comment_dtos=[],
                reaction_dtos=reaction_dtos)
        ]

        # Act
        (post_comment_count_dtos_list, post_reactions_details_dto_list,
        comment_replies_count_dto_list, comment_reactions_details_dto_list) = \
            interactor.get_user_posts_extra_dto_details_for_presenter(
                post_dtos_list=get_user_posts_dto)

        # Assert
        assert post_comment_count_dtos_list == \
             exp_post_comment_count_dtos_list
        assert post_reactions_details_dto_list == \
             exp_post_reactions_details_dto_list
        assert comment_replies_count_dto_list == \
            exp_comment_replies_count_dto_list
        assert comment_reactions_details_dto_list == \
            exp_comment_reactions_details_dto_list
    