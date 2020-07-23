import factory, factory.django

from datetime import datetime

from fb_post.models import User, Post, Comment, Reaction

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.Sequence(lambda n: "usha%d" % n)
    profile_pic = factory.Sequence(lambda n: "usha%d.com" % n)

class PostFactory(factory.Factory):
    class Meta:
        model = Post

    content = "usha"
    posted_at = factory.LazyFunction(datetime.now)
    posted_by = factory.SubFactory(UserFactory)

class CommentFactory(factory.Factory):
    class Meta:
        model = Comment

    content = "yep"
    commented_at =  factory.LazyFunction(datetime.now)
    commented_by = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)

class ReplyFactory(factory.Factory):
    class Meta:
        model = Comment

    content = "yep"
    commented_at =  factory.LazyFunction(datetime.now)
    commented_by = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
    parent_comment = factory.SubFactory(CommentFactory,
        post=factory.LazyAttribute(lambda o: o.factory_parent.comment))


class CommentReactionFactory(factory.Factory):
    class Meta:
        model = Reaction

    comment = factory.SubFactory(CommentFactory)
    reaction = factory.Iterator(["WOW","LIT","LOVE","HAHA","THUMBS-UP","THUMBS-DOWN","ANGRY","SAD"])
    reacted_at = factory.LazyFunction(datetime.now)
    reacted_by = factory.SubFactory(UserFactory)


class PostReactionsFactory(factory.Factory):
    class Meta:
        model = Reaction

    post = factory.SubFactory(PostFactory)
    reaction = factory.Iterator(["WOW","LIT","LOVE","HAHA","THUMBS-UP","THUMBS-DOWN","ANGRY","SAD"])
    reacted_at = factory.LazyFunction(datetime.now)
    reacted_by = factory.SubFactory(UserFactory)


