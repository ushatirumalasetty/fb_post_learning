"""
Get Post Details Given Valid PostId.
"""


from fb_post_clean_arch.utils.custom_test_utils_2 import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post_clean_arch.tests.views.factory.facts import *


REQUEST_BODY = """
{}
"""

TEST_CASE = {
    "request": {
        "path_params": {"post_id": "1"},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01GetPostAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE


    def setupUser(self, username, password):
        super(TestCase01GetPostAPITestCase, self).setupUser(
            username=username, password=password
        )
        print("1"*100)
        user_objs = UserFactory.create_batch(2)
        print("2"*100)
        post_obj = PostFactory.create_batch(1, user=user_objs[0])
        print("3"*100)
        comment_obj = CommentFactory.create_batch(1, post=post_obj[0])
        print("4"*100)
        reply_obj = ReplyFactory.create_batch(1, parent_comment=comment_obj[0])
        print("5"*100)
        post_reaction_obj = PostReactionsFactory.create_batch(1,post=post_obj[0], reaction_type="WOW")
        print("6"*100)
        comment_reaction_obj = PostReactionsFactory.create_batch(1,comment=comment_obj[0], reaction_type="SAD")
        print("7"*100)


    def test_case(self):
        response = self.default_test_case() 
        print("*"*100)
        print(response)
        
        # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.



