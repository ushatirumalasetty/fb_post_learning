# pylint: disable=wrong-import-position

APP_NAME = "fb_post_v2"
OPERATION_NAME = "react_to_post"
REQUEST_METHOD = "post"
URL_SUFFIX = "posts/{post_id}/react/v1/"

from .test_case_01 import TestCase01ReactToPostAPITestCase

__all__ = [
    "TestCase01ReactToPostAPITestCase"
]
