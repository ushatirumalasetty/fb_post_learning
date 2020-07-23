# pylint: disable=wrong-import-position

APP_NAME = "fb_post_v2"
OPERATION_NAME = "get_replies_for_comment"
REQUEST_METHOD = "get"
URL_SUFFIX = "comments/{comment_id}/replies/v1/"

from .test_case_01 import TestCase01GetRepliesForCommentAPITestCase

__all__ = [
    "TestCase01GetRepliesForCommentAPITestCase"
]
