# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "create_comment"
REQUEST_METHOD = "post"
URL_SUFFIX = "comments/create/v1/"

from .test_case_01 import TestCase01CreateCommentAPITestCase

__all__ = [
    "TestCase01CreateCommentAPITestCase"
]
