from fb_post_v2.models import (
    User, Post, Comment, Reaction
)
import factory
import factory.fuzzy



class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    name = "john"
    username = factory.Sequence(lambda n: "username%d" % n)
    profile_pic = "profile/user/.png"


