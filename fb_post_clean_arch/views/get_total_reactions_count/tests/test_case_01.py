"""
Get Total Reactions Count.
"""


from fb_post_clean_arch.utils.custom_test_utils_2 import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post_clean_arch.tests.views.factory.facts import *

REQUEST_BODY = """

"""

TEST_CASE = {
     "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01GetTotalReactionsCountAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01GetTotalReactionsCountAPITestCase, self).setupUser(
            username=username, password=password
        )
        PostReactionsFactory.create_batch(2)
        
        
    def test_case(self):
        print("usha tirumalasetty")
        response = self.default_test_case() 
        
        import json

        response_content = json.loads(response.content)

        count = response_content['count']

        
        self.assert_match_snapshot(
             name='count',
             value=count
        )
