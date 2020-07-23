import datetime

from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden

from fb_post_v2.constants.exception_messages import (
    INVALID_POST_ID, INVALID_COMMENT_ID
    )

from typing import List

from fb_post_v2.interactors.presenters import PresenterInterface


class PresenterImplementation(PresenterInterface):


    def get_create_post_response(self, post_id: int):
        return {
            "post_id": post_id
        }

    def get_create_comment_response(self, comment_id: int):
        return {
            "comment_id": comment_id
        }

    def raise_invalid_post_id_exception(self):
        raise NotFound(*INVALID_POST_ID)

    def raise_invalid_comment_id_exception(self):
        raise NotFound(*INVALID_COMMENT_ID)

    def get_reply_to_comment_response(self, comment_id):
        return {
            "comment_id": comment_id
        }

    def get_post_response(self,
                          get_post_dto, 
                          post_comment_count_dtos_list,
                          post_reactions_details_dto_list,
                          comment_replies_count_dto_list,
                          comment_reactions_details_dto_list):

        pass

    def _get_post_dict_details(self, get_post_dto, 
                               post_comment_count_dtos_list,
                               post_reactions_details_dto_list,
                               comment_replies_count_dto_list,
                               comment_reactions_details_dto_list):

        post = get_post_dto.post_dto
        comments = get_post_dto.comment_dtos
        reactions = get_post_dto.reaction_dtos
        users_dicts = get_post_dto.user_dtos

    
        comment_replies_count_dict = self._convert_comment_replies_into_dict(
            comment_replies_count_dto_list)
        comment_reaction_dict = self._convert_comment_reactions_to_dicts(
            comment_reactions_details_dto_list
        )

        comment_dicts = self._get_comment_dicts_details(
            comments, users_dicts,
            comment_replies_count_dict,
            comment_reaction_dict)



    return "dictionary"

    
    
    def _convert_comment_replies_into_dict(self, comment_replies_count_dtos):
        dict_form = {}
    
        for reply_count_dto in comment_replies_count_dtos:
            dto_dict = {
                reply_count_dto.comment_id: reply_count_dto
            }
            dict_form.update(dto_dict)

        return dto_dict

    def _convert_comment_reactions_to_dicts(comment_reactions_dtos):
        reaction_dicts = {}

        for reaction in comment_reactions_dtos:
            dto_dict = {
                reaction.comment_id: reaction
            }
            reaction_dicts.update(dto_dict)
        return reaction_dicts


    def _get_comment_dicts_details(
            self, comments, users_dicts,
            comment_replies_count_dict,
            comment_reaction_dict):

        comment_list = []
        comment_dtos = self._get_comments_dtos_list(comments)

        for comment_dto in comment_dtos:
    
            comment_id = comment_dto.comment_id
            comment_dict = _convert_comment_dto_to_dict(
                self, comment_dto, users_dicts)
            comment_dict['reactions'] = self._get_reactions_dict_for_comment(
                comment_reaction_dict[comment_id])
            comment_dict['replies_count'] = \
                comment_replies_count_dict[comment_id]["count"]
            comment_dict["replies"] = pass
        


    def _get_comment_replies_details(self):
        # i need to start here after the project


    def _get_reactions_dict_for_comment(self, reaction_dto):
        return {
            "count": reaction_dto.count,
            "type": reaction_dto.reaction_type
        }



    def _convert_comment_dto_to_dict(self, comment_dto, users_dicts):
        user_id = comment_dto.commented_by_id
        user_dto = users_dicts[user_dto]
        
        return {
            "comment_id": comment_dto.comment_id,
            "commenter": self._get_user_details(user_dto),
            "commented_at": self._get_date_format(comment_dto.commented_at),
            "comment_content": comment_dto.comment_content
        }



    @staticmethod
    def _get_date_format(datetime_obj):
        return datetime_obj.strftime('%Y-%m-%d %H:%M:%S.%f')

    def _get_comments_dtos_list(self, comments):
        comments_list = []

        for comment in comments:
            is_comment = comment.parent_comment_id is None
            if is_comment:
                comments_list.append(comment)

        return comments_list
  
 
    def _get_post_details(self, user_dtos_dict,
                          post_reaction_dto_dict,
                          comment_reaction_dto_dict, reply_dto_dict,
                          post_dto, comments_dto_dict):

        comments, comments_count = self._get_comment_details(
            comment_reaction_dto_dict,
            reply_dto_dict,
            comments_dto_dict,
            user_dtos_dict)

        user_id = post_dto.user_id
        user_dto = user_dtos_dict[user_id]
        post_details = {
            "post_id": post_dto.post_id,
            "posted_by": self._get_user_details(user_dto),
            "posted_at": self._get_date_format(post_dto.pub_date_time),
            "post_content": post_dto.post_content,
            "reactions": self._get_post_reactions_dict(post_dto.post_id,
                                                       post_reaction_dto_dict),
            "comments": comments,
            "comments_count": comments_count
        }
        return post_details



    @staticmethod
    def _get_user_details(user_dto):
        return {
            "user_id": user_dto.user_id,
            "name": user_dto.name,
            "profile_pic": user_dto.profile_pic
        }