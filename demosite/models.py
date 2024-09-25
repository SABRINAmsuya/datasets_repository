from django.conf import settings
from django.db import models

class Dataset(models.Model):
    PUBLIC = 'public'
    PRIVATE = 'private'
    VISIBILITY_CHOICES = [
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='datasets')
    title =models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    file = models.FileField(upload_to='datasets/')
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default=PUBLIC)

    def __str__(self):
        return self.title
    
    def is_public(self):
        return self.visibility == self.PUBLIC
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class UserDataset(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    has_access = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.dataset.title}"
    