from django.db import models

from fb_post.models.user import User


class Post(models.Model):
    content=models.CharField(max_length=1000)
    posted_at=models.DateTimeField(auto_now=True)
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
