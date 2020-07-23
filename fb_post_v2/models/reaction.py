from django.db import models

from fb_post_v2.models.user import User
from fb_post_v2.models.post import Post
from fb_post_v2.models.comment import Comment

from fb_post_v2.constants import ReactionTypeEnum


class Reaction(models.Model):

    post=models.ForeignKey(Post,on_delete=models.CASCADE, null=True)
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    reaction=models.CharField(
        max_length=100,
        choices=[
            (reaction_type.name, reaction_type.value)
            for reaction_type in ReactionTypeEnum
            ]
    )
    reacted_by=models.ForeignKey(User, on_delete=models.CASCADE)
    reacted_at=models.DateTimeField(auto_now=True)
