from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from core.user.models import User

CONTENT_TYPE_CHOICES = [('MOV', 'movie'),
                        ('TVS', 'tv show'),
                        ('DOC', 'documentary')
                        ]

class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, null=True)
    site = models.URLField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"

class Content(models.Model):
    title = models.CharField(max_length=50)
    release_year = models.IntegerField()
    description = models.TextField(max_length=255, null=True)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="content_list")
    released = models.BooleanField(default=True)
    c_type = models.CharField(choices=CONTENT_TYPE_CHOICES, max_length=25, default='MOV')
    lang = models.CharField(max_length=15, default='ENG')
    total_rating = models.IntegerField(default=0)
    count_rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}({self.release_year})"
    
class Review(models.Model):
    rating = models.PositiveBigIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=50, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="reviews")
    review_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    

    def __str__(self) -> str:
        return f"{self.rating} | {self.content.title}"

