# pylint: disable=wrong-import-position

APP_NAME = "fb_post_v2"
OPERATION_NAME = "reply_to_comment"
REQUEST_METHOD = "post"
URL_SUFFIX = "comments/{comment_id}/reply/v1/"

from .test_case_01 import TestCase01ReplyToCommentAPITestCase

__all__ = [
    "TestCase01ReplyToCommentAPITestCase"
]
