from django.db import models
import uuid

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    demo_link = models.URLField(max_length=2000,null=True,blank=True)
    source_link = models.URLField(max_length=2000,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True,editable=False,unique=True)
