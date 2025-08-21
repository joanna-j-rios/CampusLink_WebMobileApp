from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Our model for a user's task
# It maps to a table named 'core_task' in the database
class Task(models.Model):
    # This line creates a link to Django's built-in User model
    # If the user is deleted, all their tasks will be deleted too
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    # Text field for the task name
    # We set max_length to a reasonable number to prevent issues
    task_name = models.CharField(max_length=200)

    # A larger text field for the description
    # This is optional so it can be blank
    description = models.TextField(null=True, blank=True)

    # A DateField for the due date
    # This is also optional and can be blank
    due_date = models.DateField(null=True, blank=True)

    # A boolean field to track if the task is completed
    # The default value is False
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        # This makes it easier to read the model when printed in the admin site
        return self.task_name
