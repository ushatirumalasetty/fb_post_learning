import datetime

from unittest.mock import create_autospec, patch

import pytest

from django_swagger_utils.drf_server.exceptions import NotFound

from fb_post_v2.interactors.storages import PostStorageInterface

from fb_post_v2.interactors.presenters import PresenterInterface

from fb_post_v2.interactors.get_post_interactor import GetPostInteractor

from fb_post_v2.interactors.storages.dtos import (
    PostCompleteDetailsDto, PostWithCommentsCountDto,
    PostWithReactionDetailsDto, CommentWithReactionDetailsDto,
    CommentWithRepliesCountDto, CommentDto
)


@pytest.mark.django_db
class TestGetPostInteractor:


    @patch.object(GetPostInteractor,
                  'get_post_extra_details_dtos_for_presenter')
    def test_get_post_interactor_with_valid_details(self,
                                                    user_dtos,
                                                    post_dto,
                                                    comment_dtos,
                                                    reaction_dtos,
                                                    get_post_response):

        # Arrange
        post_id = 1
        expected_post_details_dict_mock = get_post_response

        post_storage = create_autospec(PostStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetPostInteractor(post_storage=post_storage,
                                       presenter=presenter)

        post_comment_count_dtos_list = [],
        post_reactions_details_dto_list = [],
        comment_replies_count_dto_list = [],
        comment_reactions_details_dto_list = []

        empty_lists = (post_comment_count_dtos_list,
                      post_reactions_details_dto_list,
                      comment_replies_count_dto_list,
                      comment_reactions_details_dto_list)

        interactor.get_post_extra_details_dtos_for_presenter.return_value = \
            empty_lists
        presenter.get_post_response.return_value = \
            expected_post_details_dict_mock
        get_post_dto = PostCompleteDetailsDto(user_dtos=user_dtos,
                                              post_dto=post_dto,
                                              comment_dtos=comment_dtos,
                                              reaction_dtos=reaction_dtos)
        post_storage.get_post_dto.return_value = get_post_dto

        # Act
        actual_post_details_dict = interactor.get_post(post_id=post_id)

        # Assert
        assert actual_post_details_dict == expected_post_details_dict_mock
        post_storage.get_post_dto.assert_called_once_with(post_id=post_id)
        presenter.get_post_response.assert_called_once_with(
            get_post_dto=get_post_dto,
            post_comment_count_dtos_list=post_comment_count_dtos_list,
            post_reactions_details_dto_list=post_reactions_details_dto_list,
            comment_replies_count_dto_list=comment_replies_count_dto_list,
            comment_reactions_details_dto_list= \
                comment_reactions_details_dto_list)


    def test_get_post_interactor_with_invalid_post_id_raise_exception(self):

        # Arrange
        invalid_post_id = -1
        post_storage = create_autospec(PostStorageInterface)
        presenter = create_autospec(PresenterInterface)
        post_storage.is_valid_post_id.return_value = False
        presenter.raise_invalid_post_id_exception.side_effect = NotFound
        interactor = GetPostInteractor(post_storage=post_storage,
                                       presenter=presenter)

        # Act
        with pytest.raises(NotFound):
            interactor.get_post(post_id=invalid_post_id)


    def test_get_post_extra_details_dtos_for_presenter(self,
                                                       user_dtos,
                                                       post_dto,
                                                       comment_dtos,
                                                       reaction_dtos):

        # Arrange
        post_id = 1

        post_storage = create_autospec(PostStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetPostInteractor(post_storage=post_storage,
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

        get_post_dto = PostCompleteDetailsDto(user_dtos=user_dtos,
                                              post_dto=post_dto,
                                              comment_dtos=comment_dtos,
                                              reaction_dtos=reaction_dtos)

        # Act
        (post_comment_count_dtos_list, post_reactions_details_dto_list,
        comment_replies_count_dto_list, comment_reactions_details_dto_list) = \
            interactor.get_post_extra_details_dtos_for_presenter(
                get_post_dto=get_post_dto)

        # Assert
        assert post_comment_count_dtos_list == \
            exp_post_comment_count_dtos_list
        assert post_reactions_details_dto_list == \
            exp_post_reactions_details_dto_list
        assert comment_replies_count_dto_list == \
            exp_comment_replies_count_dto_list
        assert comment_reactions_details_dto_list == \
            exp_comment_reactions_details_dto_list


    def test_get_post_extra_details_dtos_for_presenter_comment_with_no_replies(
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
                                datetime.datetime(2020, 10, 10, 0, 0),
                             content='HII',
                             parent_comment_id=None)
        testing_comment_dtos_list = [comment1, comment2]

        expected_comment_count_dtos = [
            CommentWithRepliesCountDto(comment_id=1, replies_count=0),
            CommentWithRepliesCountDto(comment_id=2, replies_count=0)
        ]
        post_complete_dto = PostCompleteDetailsDto(user_dtos=user_dtos,
                                                   post_dto=post_dto,
                                                   comment_dtos= \
                                                    testing_comment_dtos_list,
                                                   reaction_dtos=reaction_dtos)

        post_storage = create_autospec(PostStorageInterface)
        presenter =  create_autospec(PresenterInterface)
        interactor = GetPostInteractor(post_storage=post_storage,
                                       presenter=presenter)

        # Act
        (post_comment_count_dtos_list,
        post_reactions_details_dto_list,
        actual_comment_replies_count_dto_list,
        comment_reactions_details_dto_list) = interactor. \
            get_post_extra_details_dtos_for_presenter(post_complete_dto)

        # Assert
        assert actual_comment_replies_count_dto_list == \
            expected_comment_count_dtos


    def test_get_post_extra_details_dtos_for_presenter_with_comment_with_replies(
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
        interactor = GetPostInteractor(post_storage=post_storage,
                                       presenter=presenter)

        post_complete_dto = PostCompleteDetailsDto(user_dtos=[],
                                                   post_dto=post_dto,
                                                   comment_dtos= \
                                                   testing_comment_dtos_list,
                                                   reaction_dtos=[])

        
        # Act
        (post_comment_count_dtos_list,
        post_reactions_details_dto_list,
        actual_comment_replies_count_dto_list,
        comment_reactions_details_dto_list) = interactor. \
            get_post_extra_details_dtos_for_presenter(post_complete_dto)

        
        # Assert
        assert actual_comment_replies_count_dto_list == \
            expected_comment_count_dtos



    def test_get_post_extra_details_dtos_for_presenter_with_post_no_comments(
        self, post_dto
    ):

        # Arrrange
        expected_post_comment_count_dtos_list = [
            PostWithCommentsCountDto(post_id=1, comments_count=0)
            ]
        post_storage = create_autospec(PostStorageInterface)
        presenter =  create_autospec(PresenterInterface)
        interactor = GetPostInteractor(post_storage=post_storage,
                                       presenter=presenter)

        post_complete_dto = PostCompleteDetailsDto(user_dtos=[],
                                                   post_dto=post_dto,
                                                   comment_dtos= [],
                                                   reaction_dtos=[])

        # Act
        (actual_post_comment_count_dtos_list,
        post_reactions_details_dto_list,
        actual_comment_replies_count_dto_list,
        comment_reactions_details_dto_list) = interactor. \
            get_post_extra_details_dtos_for_presenter(post_complete_dto)

        # Assert
        assert actual_post_comment_count_dtos_list == \
            expected_post_comment_count_dtos_list


    def test_get_post_extra_details_dtos_for_presenter_with_post_with_comments(
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
        interactor = GetPostInteractor(post_storage=post_storage,
                                       presenter=presenter)

        post_complete_dto = PostCompleteDetailsDto(user_dtos=[],
                                                   post_dto=post_dto,
                                                   comment_dtos= \
                                                    comments_dtos_list,
                                                   reaction_dtos=[])

        # Act
        (actual_post_comment_count_dtos_list,
        post_reactions_details_dto_list,
        actual_comment_replies_count_dto_list,
        comment_reactions_details_dto_list) = interactor. \
            get_post_extra_details_dtos_for_presenter(post_complete_dto)

        # Assert
        assert actual_post_comment_count_dtos_list == \
            expected_post_comment_count_dtos_list


    def test_get_post_extra_details_dtos_for_presenter_with_post_with_reactions(
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
        interactor = GetPostInteractor(post_storage=post_storage,
                                       presenter=presenter)

        post_complete_dto = PostCompleteDetailsDto(
            user_dtos=user_dtos,
            post_dto=post_dto,
            comment_dtos=comment_dtos,
            reaction_dtos= \
                post_reactions_dtos_with_duplicates)

        # Act
        (post_comment_count_dtos_list,
        actual_post_reactions_details_dto_list,
        comment_replies_count_dto_list,
        comment_reactions_details_dto_list) = interactor. \
            get_post_extra_details_dtos_for_presenter(post_complete_dto)

        # Assert
        assert actual_post_reactions_details_dto_list == \
            expected_post_comment_count_dtos_list


    def test_get_post_extra_details_dtos_for_presenter_with_post_no_reactions(
        self, post_dto, user_dtos, comment_dtos
    ):

        # Arrrange
        expected_post_comment_count_dtos_list = [
            PostWithReactionDetailsDto(post_id=1, reaction_type=[], count=0)
            ]
        post_storage = create_autospec(PostStorageInterface)
        presenter =  create_autospec(PresenterInterface)
        interactor = GetPostInteractor(post_storage=post_storage,
                                       presenter=presenter)

        post_complete_dto = PostCompleteDetailsDto(user_dtos=user_dtos,
                                                   post_dto=post_dto,
                                                   comment_dtos=comment_dtos,
                                                   reaction_dtos=[])

        # Act
        (post_comment_count_dtos_list,
        actual_post_reactions_details_dto_list,
        comment_replies_count_dto_list,
        comment_reactions_details_dto_list) = interactor. \
            get_post_extra_details_dtos_for_presenter(post_complete_dto)

        # Assert
        assert actual_post_reactions_details_dto_list == \
            expected_post_comment_count_dtos_list


    def test_get_post_extra_details_dtos_for_presenter_with_comment_with_reactions(
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
        interactor = GetPostInteractor(post_storage=post_storage,
                                       presenter=presenter)

        post_complete_dto = PostCompleteDetailsDto(
            user_dtos=user_dtos,
            post_dto=post_dto,
            comment_dtos=comment_dtos,
            reaction_dtos= \
                comment_reactions_dtos_with_duplicates)

        # Act
        (post_comment_count_dtos_list,
        post_reactions_details_dto_list,
        comment_replies_count_dto_list,
        actual_comment_reactions_details_dto_list) = interactor. \
            get_post_extra_details_dtos_for_presenter(post_complete_dto)

        # Assert
        assert actual_comment_reactions_details_dto_list == \
            expected_comment_reactions_details_dto_list



    def test_get_post_extra_details_dtos_for_presenter_with_comment_with_no_reactions(
        self, post_dto, user_dtos,
        post_reactions_dtos_with_duplicates
    ):

        # Arrrange
        empty_comment_dtos = []
        expected_comment_reactions_details_dto_list = []
        post_storage = create_autospec(PostStorageInterface)
        presenter =  create_autospec(PresenterInterface)
        interactor = GetPostInteractor(post_storage=post_storage,
                                       presenter=presenter)

        post_complete_dto = PostCompleteDetailsDto(
            user_dtos=user_dtos,
            post_dto=post_dto,
            comment_dtos=empty_comment_dtos,
            reaction_dtos= \
                post_reactions_dtos_with_duplicates)

        # Act
        (post_comment_count_dtos_list,
        post_reactions_details_dto_list,
        comment_replies_count_dto_list,
        actual_comment_reactions_details_dto_list) = interactor. \
            get_post_extra_details_dtos_for_presenter(post_complete_dto)

        # Assert
        assert actual_comment_reactions_details_dto_list == \
            expected_comment_reactions_details_dto_list