from django.db.models import Count, Q, F, Prefetch

from typing import List, Dict, Optional

from fb_post_v2.models import Post, User, Reaction, Comment

from fb_post_v2.interactors.storages import StorageInterface
from fb_post_v2.interactors.storages import PostStorageInterface
from fb_post_v2.interactors.storages import ReactionStorageInterface
from fb_post_v2.interactors.storages import CommentStorageInterface

from fb_post_v2.constants import ReactionTypeEnum

from fb_post_v2.exceptions import ReactionDoesNotExists

from fb_post_v2.constants import (
    POSITIVE_REACTIONS_ENUMS, NEGATIVE_REACTIONS_ENUMS
)

from fb_post_v2.interactors.storages.dtos import (
    TotalReactionCountDto, ReactionMetricsDto,
    PostCompleteDetailsDto, ReactionDto, CommentDto,
    UserDto, PostDto, PostWithCommentsCountDto, PostWithReactionDetailsDto,
    CommentWithReactionDetailsDto, CommentWithRepliesCountDto, PostReactionsDto
    )


class StorageImplementation(StorageInterface):

    def create_post(self, user_id: int, post_content: str) ->int:

        post = Post.objects.create(posted_by_id=user_id,
                                   content=post_content)
        post_id = post.id
        return post_id

    def is_valid_post_id(self, post_id: int):
        is_valid_post_id = Post.objects.filter(id=post_id).exists()
        return is_valid_post_id

    def is_valid_comment_id(self, comment_id: int):
        is_valid_comment_id = Comment.objects.filter(id=comment_id).exists()
        return is_valid_comment_id

    def create_comment(self, user_id: int,
                       post_id:int, comment_content: str) ->int:

        comment = Comment.objects.create(commented_by_id=user_id,
                                         post_id=post_id,
                                         content=comment_content)
        comment_id = comment.id
        return comment_id

    def reply_to_comment(self, user_id: int, comment_id: int,
                         reply_content: str) ->int:

        comment_obj = Comment.objects.get(id=comment_id)
        comment = Comment.objects.create(commented_by_id=user_id,
                                            post_id=comment_obj.post_id,
                                            content=reply_content,
                                            parent_comment_id=comment_id)
        return comment.id

    def return_comment_id_if_is_comment_id_or_return_parent_comment_id(
            self, comment_id: int
    ) ->int:

        comment = Comment.objects.get(id=comment_id)
        is_comment = comment.parent_comment_id is None

        if is_comment:
            return comment_id
        return comment.parent_comment_id

    def validate_post_reaction_if_exists_get_reaction_type(
            self,
            user_id: int,
            post_id: int# no need of reaction type here change in test cases alse
    ):

        reaction_objs = Reaction.objects.filter(reacted_by_id=user_id,
                                           post_id=post_id)
        is_reaction_exists = reaction_objs.exists()
        if is_reaction_exists:
            return reaction_objs.first().reaction

        raise ReactionDoesNotExists

    def validate_comment_reaction_if_exists_get_reaction_type(
            self,
            user_id: int,
            comment_id: int# no need of reaction type here change in test cases alse
    ):

        reaction_objs = Reaction.objects.filter(reacted_by_id=user_id,
                                                comment_id=comment_id)
        is_reaction_exists = reaction_objs.exists()
        if is_reaction_exists:
            return reaction_objs.first().reaction

        raise ReactionDoesNotExists


    def create_reaction_to_post(self, user_id: int, post_id: int,
                                reaction_type: ReactionTypeEnum):

        reaction = Reaction.objects.create(reacted_by_id=user_id,
                                           post_id=post_id,
                                           reaction=reaction_type)
        return reaction.id


    def create_reaction_to_comment(self,
                                  user_id: int,
                                  comment_id: int,
                                  reaction_type: ReactionTypeEnum):

        reaction = Reaction.objects.create(reacted_by_id=user_id,
                                           comment_id=comment_id,
                                           reaction=reaction_type)
        return reaction.id


    def undo_post_reaction(self,
                           user_id: int,
                           post_id: int):

        Reaction.objects.get(reacted_by_id=user_id,
                             post_id=post_id).delete()

    def undo_comment_reaction(self,
                           user_id: int,
                           comment_id: int):

        Reaction.objects.get(reacted_by_id=user_id,
                             comment_id=comment_id).delete()

    def update_post_reaction(self,
                             user_id: int,
                             post_id: int,
                             reaction_type: ReactionTypeEnum):

        Reaction.objects.filter(reacted_by_id=user_id,
                                post_id=post_id).update(
            reaction=reaction_type)


    def update_comment_reaction(self,
                                user_id: int,
                                comment_id: int,
                                reaction_type: ReactionTypeEnum):

        Reaction.objects.filter(reacted_by_id=user_id,
                                comment_id=comment_id).update(
            reaction=reaction_type)


    def get_total_reaction_count_dto(self):

        count_dict = Reaction.objects.aggregate(count=Count("reacted_by"))

        return TotalReactionCountDto(count=count_dict["count"])

    def get_reaction_metrics_dto(self,
                                 post_id: int) ->List[ReactionMetricsDto]:

        reaction_metrics_list = Reaction.objects.filter(post_id=post_id) \
                                        .values_list('reaction') \
                                        .annotate(
                                            count=Count('reaction')
                                        )
        dtos_list = [
             ReactionMetricsDto(reaction_type=react_metric[0],
                                count=react_metric[1])
             for react_metric in reaction_metrics_list
        ]
        return dtos_list


    def is_post_created_by_user(self, user_id: int, post_id: int):

        is_post_created_by_user = Post.objects.filter(id=post_id,
                                                      posted_by_id=user_id
                                                      ).exists()
        return is_post_created_by_user


    def delete_post(self, post_id: int):

        Post.objects.get(id=post_id).delete()


    def get_posts_with_more_positive_reactions(self) ->List[Optional[int]]:

        num_positive = Count('reaction',
                             filter=Q(reaction__in=POSITIVE_REACTIONS_ENUMS))
        num_negative = Count('reaction',
                             filter=Q(reaction__in=NEGATIVE_REACTIONS_ENUMS))
    
        post_ids_list = list(Reaction.objects \
                                     .select_related(
                                         'post')\
                                     .values('post_id')\
                                     .annotate(
                                         num_positive=num_positive,
                                         num_negative=num_negative
                                     ).filter(num_positive__gt=num_negative) \
                                     .values_list('post_id', flat=True)
        )
        post_ids_list.remove(None)
        return post_ids_list


    def get_posts_reacted_by_user(self, user_id: int) ->List[Optional[int]]:

        post_ids_list = list(Post.objects \
                                 .filter(posted_by_id=user_id)\
                                 .values_list('id',flat=True)
        )
        return post_ids_list


    def get_post_dto(self, post_id: int) ->PostCompleteDetailsDto:
        comment_query_set = Comment.objects\
                                   .select_related('commented_by')\
                                   .prefetch_related('reaction_set')

        post = Post.objects\
                   .select_related('posted_by')\
                   .prefetch_related(
                        'reaction_set',
                        Prefetch(
                            'comment_set',
                            queryset=comment_query_set)
                    ).get(pk=post_id)

        get_post_details_dto_obj = self._get_post_details_dto_obj(post)
        return get_post_details_dto_obj


    def _get_post_details_dto_obj(self, post):

        post_user_dto_dict = {}
        post_dto = self._convert_post_obj_to_dto(post)
        post_reaction_dtos = self._get_post_reactions(post)
       
        user_obj = post.posted_by
        user_dto = self._convert_user_obj_to_dto(user_obj)
        user_id = user_dto.user_id
        post_user_dto_dict[user_id] = user_dto

        comments = post.comment_set.all()
        comments_list = self._get_comments_only(comments)
        users_dto_dict, comment_dtos_list, comment_reaction_dtos = \
            self._get_comments_details(comments_list)

        reply_user_dtos_dict, reply_dtos, reply_reaction_dtos = \
             self._get_replies_details(comments)

        comment_reaction_dtos = \
            self._merge_comment_reactions_dtos_and_reply_reactions_dtos(
            comment_reaction_dtos, reply_reaction_dtos)
        comment_dtos = self._merge_comment_dtos_and_reply_dtos(
            comment_dtos_list, reply_dtos)

        users_dto_dict.update(post_user_dto_dict)
        users_dto_dict.update(reply_user_dtos_dict)
        user_dtos = list(users_dto_dict.values())

        reaction_dtos = self._merge_post_reaction_dtos_and_comment_reaction_dtos(
            post_reaction_dtos, comment_reaction_dtos
            )

        post_details_dto = PostCompleteDetailsDto(post_dto=post_dto,
                                                  user_dtos=user_dtos,
                                                  comment_dtos=comment_dtos,
                                                  reaction_dtos=reaction_dtos)
        return post_details_dto

    def _get_comments_only(self, comments):
        comments_list = []

        for comment in comments:
            is_comment = comment.parent_comment_id is None
            if is_comment:
                comments_list.append(comment)
        return comments_list

    def _get_replies_only(self, comments):
        replies_list = []

        for comment in comments:
            is_comment = comment.parent_comment_id is not None
            if is_comment:
                replies_list.append(comment)
        return replies_list


    @staticmethod
    def _merge_post_reaction_dtos_and_comment_reaction_dtos(
        post_reaction_dtos, comment_reaction_dtos
    ):
        reaction_dtos = post_reaction_dtos + comment_reaction_dtos
        return reaction_dtos
        
    @staticmethod
    def _merge_comment_dtos_and_reply_dtos(comment_dtos, reply_dtos):
        comment_dtos = comment_dtos + reply_dtos
        return comment_dtos

    @staticmethod
    def _merge_comment_reactions_dtos_and_reply_reactions_dtos(
            comment_reaction_dtos, reply_reaction_dtos):
        comment_reaction_dtos = comment_reaction_dtos + reply_reaction_dtos
        return comment_reaction_dtos


    # def _get_replies_details(self, comments):
    #     users_dicts_dtos = {} # need to add user dto also
    #     reply_dtos = []
    #     reply_reaction_dtos = []

    #     for comment in comments:
    #         replies_users_dto_dict, comment_dto, comment_reaction_dto = \
    #             self._get_reply_details(comment.id, comments)
    #         reply_dtos += comment_dto
    #         reply_reaction_dtos += comment_reaction_dto
    #         users_dicts_dtos.update(replies_users_dto_dict)
    #         # update user dto also
    #     return users_dicts_dtos, reply_dtos, reply_reaction_dt

    #def _get_replies_for_comment(self, comment_id, comments):
        replies_list = []

        for comment in comments:
            is_reply_for_commnet_id = comment.parent_comment_id == comment_id
            if is_reply_for_commnet_id:
                replies_list.append(comment)

        return replies_list

    def _get_replies_details(self, comments):
        users_dto_dict = {}
        reply_dtos = []
        reply_reaction_dtos = []

        replies = self._get_replies_only(comments)
        reply_dtos = self._get_reply_dtos(replies)

        reply_reaction_dtos += self._get_reply_reaction_dtos(replies)# i am here afternoon
        replies_users_dto_dict = self._add_reply_users_to_user_dto_dict(
            replies, users_dto_dict)
        return replies_users_dto_dict, reply_dtos, reply_reaction_dtos


    def _add_reply_users_to_user_dto_dict(self, replies, users_dto_dict):

        for reply in replies:
            user_obj = reply.commented_by
            user_dto = self._convert_user_obj_to_dto(user_obj)
            user_id = user_dto.user_id
            users_dto_dict[user_id] = user_dto
        return users_dto_dict


    def _get_reply_reaction_dtos(self, replies):
        reply_reaction_dtos = []

        for reply in replies:
            reply_reactions = reply.reaction_set.all()
            reaction_dtos = self._convert_reaction_objects_to_dtos(
                reply_reactions
            )
            reply_reaction_dtos += reaction_dtos

        return reply_reaction_dtos


    def _get_reply_dtos(self, replies):
        reply_dtos = []
        for reply in replies:
            comment_dto =  self._convert_reply_obj_to_dto(reply)
            reply_dtos.append(comment_dto)
        return reply_dtos

    @staticmethod
    def _convert_reply_obj_to_dto(reply):
        reply_dto = CommentDto(comment_id=reply.id,
                               commented_by_id=reply.commented_by_id,
                               post_id=reply.post_id,
                               commented_at=reply.commented_at.replace(
                                   tzinfo=None),
                               content=reply.content,
                               parent_comment_id=reply.parent_comment_id)
        return reply_dto


    def _get_post_reactions(self, post):
        post_reactions_objs = post.reaction_set.all()

        post_reaction_dtos = [
            self._convert_post_reaction_obj_to_dto(reaction)
            for reaction in post_reactions_objs
            ]
        return post_reaction_dtos

    def _get_comment_details(self, comment):
        users_dto_dict = {}
        comment_dtos = []
        comments_reaction_dtos = []

        comment_dto = self._convert_comment_obj_to_dto(comment)
        comment_dtos.append(comment_dto)
        
        comment_user = comment.commented_by
        user_dto = self._convert_user_obj_to_dto(comment_user)
        user_id = user_dto.user_id
        users_dto_dict[user_id] = user_dto

        comment_reactions = comment.reaction_set.all()
        comments_reaction_dtos = self._convert_reaction_objects_to_dtos(
            comment_reactions
        )

        return users_dto_dict, comment_dtos, comments_reaction_dtos # need to update it

    def _get_comments_details(self, comments):

        users_dtos_dict = {}
        comments_dtos = []
        comments_reaction_dtos = []

        for comment in comments:
            user_dto_dict, comment_dto, comment_reaction_dto = \
                self._get_comment_details(comment)
            comments_dtos += comment_dto
            comments_reaction_dtos += comment_reaction_dto
            users_dtos_dict.update(user_dto_dict)

        return users_dtos_dict, comments_dtos, comments_reaction_dtos




    def _convert_reaction_objects_to_dtos(self, reactions):
        reaction_dtos = []
        
        for reaction in reactions:
            reaction_dto = self._convert_comment_reaction_object_to_dto(
                reaction)
            reaction_dtos.append(reaction_dto)
        return reaction_dtos


    @staticmethod
    def _convert_comment_reaction_object_to_dto(reaction):
        reaction_dto = ReactionDto(reaction_id=reaction.id,
                                   reacted_by_id=reaction.reacted_by_id,
                                   comment_id=reaction.comment_id,
                                   reacted_at=reaction.reacted_at,
                                   post_id=reaction.post_id,
                                   reaction=reaction.reaction)
        return reaction_dto


    @staticmethod
    def _convert_comment_obj_to_dto(comment):
        comment_dto = CommentDto(comment_id=comment.id,
                                 commented_by_id=comment.commented_by_id,
                                 post_id=comment.post_id,
                                 commented_at=comment.commented_at.replace(
                                     tzinfo=None),
                                 content=comment.content,
                                 parent_comment_id=comment.parent_comment_id)
        return comment_dto


    @staticmethod
    def _convert_post_obj_to_dto(post):
        post_dto = PostDto(posted_by_id=post.posted_by_id,
                           posted_at=post.posted_at.replace(tzinfo=None),
                           post_id=post.id,
                           content=post.content)
        return post_dto

    @staticmethod
    def _convert_post_reaction_obj_to_dto(reaction):
        reaction_dto = ReactionDto(reaction_id=reaction.id,
                                   reacted_by_id=reaction.reacted_by_id,
                                   post_id=reaction.post_id,
                                   comment_id=reaction.comment_id,
                                   reacted_at=reaction.reacted_at,
                                   reaction=reaction.reaction)
        return reaction_dto

    @staticmethod
    def _convert_user_obj_to_dto(user):
        user_dto = UserDto(user_id=user.id,
                           name=user.name,
                           profile_pic=user.profile_pic)
        return user_dto


    def get_reactions_to_post_dto(self, post_id: int) ->List[PostReactionsDto]:

        post_reaction_dtos_list = []

        post_reactions = Reaction.objects.filter(post_id=post_id) \
                                 .select_related('reacted_by')
 
        for reaction in post_reactions:
            reaction_user = reaction.reacted_by
            user_dto = self._convert_user_obj_to_dto(reaction_user)
            post_reaction_dto = PostReactionsDto(user_dto=user_dto,
                                            reaction=reaction.reaction)
            post_reaction_dtos_list.append(post_reaction_dto)

        return post_reaction_dtos_list
