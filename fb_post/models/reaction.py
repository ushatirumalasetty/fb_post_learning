from django.db import models

from fb_post.models.user import User
from fb_post.models.post import Post
from fb_post.models.comment import Comment

from fb_post.constants.enum_constants import ReactionTypeChoices


class Reaction(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE,null=True)
    reaction=models.CharField(
        max_length=100,
        choices=[
            (reaction_type.name, reaction_type.value)
            for reaction_type in ReactionTypeChoices
            ]
    )
    reacted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    reacted_at=models.DateTimeField(auto_now=True)
