
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        title = models.CharField(max_length=255)
        content = models.TextField()
        timestamp = models.DateTimeField(auto_now_add=True)
        is_event = models.BooleanField(default=False)

        def __str__(self):
            return self.title
    