# pylint: disable=wrong-import-position

APP_NAME = "fb_post_v2"
OPERATION_NAME = "react_to_comment"
REQUEST_METHOD = "post"
URL_SUFFIX = "comments/{comment_id}/react/v1/"

from .test_case_01 import TestCase01ReactToCommentAPITestCase

__all__ = [
    "TestCase01ReactToCommentAPITestCase"
]
