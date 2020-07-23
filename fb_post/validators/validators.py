from fb_post.models import *
from fb_post.validators.exceptions import *

def is_valid_post(post_id):

    try:
        post = Post.objects.get(pk=post_id)

    except Post.DoesNotExist:
        raise InvalidPostException

    return post

def is_valid_user(user_id):

    try:
        user = User.objects.get(pk=user_id)

    except User.DoesNotExist:
        raise InvalidUserException

    return user


def is_valid_comment(comment_id):
    
    try:
        comment = Comment.objects.get(pk=comment_id)

    except Comment.DoesNotExist:
        raise InvalidCommentException

    return comment


def is_valid_comment_content(comment_content):

    if comment_content == "":
        raise InvalidCommentContent


def is_valid_post_content(post_content):

 if post_content == '':
        raise InvalidPostContent
