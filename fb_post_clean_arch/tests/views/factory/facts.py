import factory, factory.django

from datetime import datetime

from fb_post_clean_arch.models import User, Post, Comment, Reactions


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
   
    username = factory.Sequence(lambda n : "usha%d" % n)
    name = factory.Sequence(lambda n: "ammudu%d" % n)
    profile_pic = factory.Sequence(lambda n: "usha%d.com" % n)

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    post_content = "usha"
    pub_date_time = factory.LazyFunction(datetime.now)
    user = factory.SubFactory(UserFactory)

class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    comment_text = "yep"
    pub_date_time =  factory.LazyFunction(datetime.now)
    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)

class ReplyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    comment_text = "yep"
    pub_date_time =  factory.LazyFunction(datetime.now)
    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
    parent_comment = factory.SubFactory(CommentFactory,
    post=factory.LazyAttribute(lambda o: o.factory_parent.comment))


class CommentReactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reactions

    comment = factory.SubFactory(CommentFactory)
    reaction_type = factory.Iterator(["WOW","LIT","LOVE","HAHA","THUMBS-UP","THUMBS-DOWN","ANGRY","SAD"])
    user = factory.SubFactory(UserFactory)


class PostReactionsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reactions

    post = factory.SubFactory(PostFactory)
    reaction_type = factory.Iterator(["WOW","LIT","LOVE","HAHA","THUMBS-UP","THUMBS-DOWN","ANGRY","SAD"])
    user = factory.SubFactory(UserFactory)
