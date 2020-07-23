from django.db import models

REACTION_CHOICES=[
    ('WOW','WOW'),
    ('LIT','LIT'),
    ('LOVE','LOVE'),
    ('HAHA','HAHA'),
    ('THUMBS-UP','THUMBS-UP'),
    ('THUMBS-DOWN','THUMBS-DOWN'),
    ('ANGRY','ANGRY'),
    ('SAD','SAD')
    ]

class User(models.Model):
    name=models.CharField(max_length=100)
    profile_pic=models.TextField()
    
class Post(models.Model):
    content=models.CharField(max_length=1000)
    posted_at=models.DateTimeField(auto_now=True)
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    
class Comment(models.Model):
    content=models.CharField(max_length=1000)
    commented_at=models.DateTimeField(auto_now=True)
    commented_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    parent_comment=models.ForeignKey('self',on_delete=models.CASCADE,related_name='comments',null=True)

class Reaction(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE,null=True)
    reaction=models.CharField(max_length=100,choices=REACTION_CHOICES)
    reacted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    reacted_at=models.DateTimeField(auto_now=True)
    
    
