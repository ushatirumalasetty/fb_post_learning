# pylint: disable=wrong-import-position

APP_NAME = "fb_post_v2"
OPERATION_NAME = "get_reaction_metrics"
REQUEST_METHOD = "get"
URL_SUFFIX = "posts/{post_id}/reaction/metrics/v1/"

from .test_case_01 import TestCase01GetReactionMetricsAPITestCase

__all__ = [
    "TestCase01GetReactionMetricsAPITestCase"
]
