from django.db import models


# databases

class Post(models.Model):
    content: str = models.TextField(null=False)
    

    