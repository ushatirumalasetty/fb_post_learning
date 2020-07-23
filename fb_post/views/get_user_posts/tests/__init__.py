# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "get_user_posts"
REQUEST_METHOD = "get"
URL_SUFFIX = "users/posts/v1/"

from .test_case_01 import TestCase01GetUserPostsAPITestCase

__all__ = [
    "TestCase01GetUserPostsAPITestCase"
]
