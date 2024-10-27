from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField()
    uploaded_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image by {self.user.username} uploaded on {self.uploaded_at}"

# Create your models here.
