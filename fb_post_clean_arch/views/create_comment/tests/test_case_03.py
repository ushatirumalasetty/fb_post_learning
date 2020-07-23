"""
Create Comment Given Valid PostId And Return CommentId.
"""
import datetime
from fb_post_clean_arch.models import Comment, Post, User
from fb_post_clean_arch.utils.custom_test_utils_2 import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


import factory

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    name = factory.Sequence(lambda n: "user%d" % n)
    profile_pic = factory.Sequence(lambda n: "profile_pic/user%d.png" % n)


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
    user = factory.SubFactory(UserFactory)
    post_content = factory.Sequence(lambda n: "post content%d" % n)
    pub_date_time = factory.LazyFunction(datetime.datetime.now)



REQUEST_BODY = """
{
    "post_id": 1,
    "comment_text": "string"
}
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


class TestCase03CreateCommentAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase03CreateCommentAPITestCase, self).setupUser(
            username=username, password=password
        )
        PostFactory()

    def test_case(self):
        print("@@@@@@@@@@@@@@@@@@@@@")
        response = self.default_test_case()
        import json

        response_content = json.loads(response.content)

        comment_id = response_content['comment_id']

        comment = Comment.objects.get(id=comment_id)

        self.assert_match_snapshot(
            name='user_id',
            value=comment.user.id
        )

        self.assert_match_snapshot(
            name='post_id',
            value=comment.post.id
        )
        self.assert_match_snapshot(
            name='comment_text',
            value=comment.comment_text
        )
