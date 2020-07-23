# pylint: disable=wrong-import-position

APP_NAME = "fb_post_v2"
OPERATION_NAME = "get_total_reaction_count"
REQUEST_METHOD = "get"
URL_SUFFIX = "reactions/count/v1/"

from .test_case_01 import TestCase01GetTotalReactionCountAPITestCase

__all__ = [
    "TestCase01GetTotalReactionCountAPITestCase"
]
