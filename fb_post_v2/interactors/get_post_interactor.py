from fb_post_v2.interactors.storages import PostStorageInterface

from fb_post_v2.interactors.presenters import PresenterInterface

from fb_post_v2.interactors.storages.dtos import (
    PostCompleteDetailsDto, PostWithCommentsCountDto,
    PostWithReactionDetailsDto, CommentWithReactionDetailsDto,
    CommentWithRepliesCountDto
)


class GetPostInteractor:

    def __init__(self,
                 post_storage: PostStorageInterface,
                 presenter: PresenterInterface):

        self.post_storage = post_storage
        self.presenter = presenter

    def get_post(self, post_id: int) ->PostCompleteDetailsDto:# -done TODO mention returning type

        is_valid_post_id = self.post_storage.is_valid_post_id(post_id=post_id)
        invalid_post_id_given = not is_valid_post_id

        if invalid_post_id_given:
            self.presenter.raise_invalid_post_id_exception()
            return

        get_post_dto = self.post_storage.get_post_dto(post_id=post_id)
        
        (post_with_comments_count_dtos_list,
        post_with_reactions_details_dtos_list,
        comment_with_replies_count_dtos_list,
        comment_with_reactions_details_list) = \
            self.get_post_extra_details_dtos_for_presenter(get_post_dto)


            # need to send it to response
        response = self.presenter.get_post_response(
            get_post_dto = get_post_dto,
            post_comment_count_dtos_list=post_with_comments_count_dtos_list,
            post_reactions_details_dto_list=post_with_reactions_details_dtos_list,
            comment_replies_count_dto_list=comment_with_replies_count_dtos_list,
            comment_reactions_details_dto_list=comment_with_reactions_details_list
        )
        return response



    def get_post_extra_details_dtos_for_presenter(
        self, get_post_dto: PostCompleteDetailsDto
    ):

        post_with_comments_count_dtos_list = []
        post_with_reactions_details_dtos_list = []
        comment_with_replies_count_dtos_list = []
        comment_with_reactions_details_list = []

        post_id = get_post_dto.post_dto.post_id
        comments = get_post_dto.comment_dtos
        reactions = get_post_dto.reaction_dtos

        
        comment_with_replies_count_dtos_list = \
            self._get_comment_with_replies_count_dtos(comments)
        
        post_reactions_details_dto = self._get_post_reaction_details_dto(
            post_id, reactions)
        post_with_reactions_details_dtos_list.append(post_reactions_details_dto)

        comment_reactions_dtos_list = \
            self._get_comment_with_reaction_details_dtos(comments, reactions)
        comment_with_reactions_details_list = comment_reactions_dtos_list

        post_with_comments_count_dtos_list = self._get_post_comments_count_dtos(
            post_id, comment_with_replies_count_dtos_list)

        return (post_with_comments_count_dtos_list,
                post_with_reactions_details_dtos_list,
                comment_with_replies_count_dtos_list,
                comment_with_reactions_details_list)


    def _get_post_comments_count_dtos(self, post_id, comments_dtos):
        count = len(comments_dtos)
        
        post_with_comments_count_dtos_list = [
            PostWithCommentsCountDto(post_id=post_id,
                                     comments_count=count)
        ]
        
        return post_with_comments_count_dtos_list
    
    def _get_comment_with_replies_count_dtos(self, comments):
        dtos_list = []

        for comment in comments:
            if self.is_comment(comment):
                replies_count =  self._get_replies_count(comment.comment_id, comments)
                dto = CommentWithRepliesCountDto(comment_id=comment.comment_id,
                                                 replies_count=replies_count)
                dtos_list.append(dto)
        return dtos_list

    def _get_comment_with_reaction_details_dtos(self, comments, reactions):
        reactions_dtos_list = []

        for comment in comments:
            count, reactions_list = self._get_comment_id_reactions_details(
                comment.comment_id, reactions)
            dto = CommentWithReactionDetailsDto(comment_id=comment.comment_id,
                                                reaction_type=reactions_list,
                                                count=count)
            reactions_dtos_list.append(dto)
        return reactions_dtos_list

    def _get_comment_id_reactions_details(self, comment_id, reactions):
        reactions_list = []

        for reaction in reactions:
            is_comment_reaction = reaction.comment_id == comment_id
            if is_comment_reaction:
                reactions_list.append(reaction.reaction)

        count = len(reactions_list)
        reactions_list = list(set(reactions_list))
        reactions_list.sort()

        return count, reactions_list

    def _get_post_reaction_details_dto(self, post_id, reactions):
        reactions_list = []
    
        for reaction in reactions:
            is_post_reaction = reaction.post_id == post_id
            if is_post_reaction:
                reactions_list.append(reaction.reaction)

        count = len(reactions_list)
        reactions_list = list(set(reactions_list))
        reactions_list.sort()
        dto = PostWithReactionDetailsDto(post_id=post_id,
                                         reaction_type=reactions_list,
                                         count=count)
        return dto

    def _get_replies_count(self, comment_id, comments):
        count = 0
        for comment in comments:
            is_reply_for_commnet_id = comment.parent_comment_id == comment_id
            if is_reply_for_commnet_id:
                count = count + 1
        return count

    @staticmethod
    def is_comment(comment):
        is_comment = comment.parent_comment_id is None
        return is_comment

