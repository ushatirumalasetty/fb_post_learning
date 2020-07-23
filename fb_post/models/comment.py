from django.db import models

from fb_post.models.user import User
from fb_post.models.post import Post


class Comment(models.Model):
    content=models.CharField(max_length=1000)
    commented_at=models.DateTimeField(auto_now=True)
    commented_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    parent_comment=models.ForeignKey('self',on_delete=models.CASCADE,related_name='comments',null=True)
