from django.db import models

# Create your models here.
class Content(models.Model):
    Title = models.CharField(max_length=255, null=False)
    CreateDate = models.DateTimeField(auto_now_add=True)
    Detail = models.TextField()
    Name_image = models.CharField(max_length=255, null=True)

