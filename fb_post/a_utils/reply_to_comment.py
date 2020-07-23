from fb_post.models import Comment
from fb_post.exceptions import InvalidReplyContent
from .utils_validators import is_valid_user, is_valid_comment



def is_valid_reply_content(reply_content):

    if reply_content == '':
        raise InvalidReplyContent


def is_it_comment(comment):
    if comment.parent_comment_id is None:
        return True

    return False

def is_it_reply(comment):
    if comment.parent_comment_id is None:
        return False

    return True



#4
def reply_to_comment(user_id, comment_id, reply_content):

    is_valid_user(user_id)
    is_valid_reply_content(reply_content)
    comment = is_valid_comment(comment_id)


    if is_it_comment(comment): # TODO: Duplication of code
        comment_reply = Comment.objects.create(content=reply_content,
                                               commented_by_id=user_id,
                                               post_id=comment.post_id,
                                               parent_comment_id=comment_id)
    elif is_it_reply(comment):
        comment_reply = Comment.objects.create(content=reply_content,
                                               commented_by_id=user_id,
                                               post_id=comment.post_id,
                                               parent_comment_id=(
                                                   comment.parent_comment_id)
                                              )

    return comment_reply.id
