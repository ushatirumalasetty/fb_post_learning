"""
React To Post Given Valid PostId Creates Reaction
"""

from fb_post_clean_arch.utils.custom_test_utils_2 import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post_clean_arch.tests.views.factory.facts import *


REQUEST_BODY = """
{
    "reaction_type": "HAHA"
}
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


class TestCase01ReactToPostAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01ReactToPostAPITestCase, self).setupUser(
            username=username, password=password
        )
        
        post = PostFactory()
        print(post)
        
    def test_case(self):
        self.default_test_case()
        print("*"*40)
        reaction=Reactions.objects.get(post_id=1, user_id=2, reaction_type="WOW")
        user_id = reaction.user.id
        post_id = reaction.post.id
        reaction_type = reaction.reaction_type

        self.assert_match_snapshot(
             name='user_id',
             value=user_id
        )

        self.assert_match_snapshot(
             name='post_id',
             value=post_id
        )
        self.assert_match_snapshot(
            name='comment_text',
            value=reaction_type
        )
