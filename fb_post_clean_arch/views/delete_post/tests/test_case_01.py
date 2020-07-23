"""
Delete Post Given Valid UserId, PostId.
"""


from fb_post_clean_arch.utils.custom_test_utils_2 import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post_clean_arch.tests.views.factory.facts import *
from fb_post_clean_arch.models import Post


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



class TestCase01DeletePostAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01DeletePostAPITestCase, self).setupUser(
            username=username, password=password
        )
        print("yeppppppppppppppppppppp")

        PostFactory()
        print("yeppppppppppppppppppppp")
    
    def test_case(self):
        print("yeppppppppppppppppppppp")
        self.default_test_case()
        print("yeppppppppppppppppppppp")
        posts= Post.objects.all()    
        self.assert_match_snapshot(
            name='posts',
            value=posts
        )

        
        