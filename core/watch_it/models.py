from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from core.user.models import User
from datetime import timedelta
import uuid
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os
from PIL import Image
CONTENT_TYPE_CHOICES = [('MOV', 'movie'),
                        ('TVS', 'tv show'),
                        ('DOC', 'documentary')
                        ]
CONTENT_CERTIFICATES = [
    ('U', 'unrestricted public exhibition (U)'),
    ('U/A', 'parental guidance for children below age 12 (U/A)'),
    ('A', 'adult (A)'),
    ('S', 'viewing by specialised groups (S)')
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
    certificate = models.CharField(choices=CONTENT_CERTIFICATES, default='U', max_length=5)
    duration = models.DurationField(default=timedelta(minutes=1))
    trailer_link = models.URLField(default='https://www.youtube.com/')

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

def content_picture_upload_path(instance, filename):
    return f"{instance.content.title}/{uuid.uuid4()}_{filename}"

class ContentPicture(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='pictures')
    picture = models.ImageField(upload_to=content_picture_upload_path)

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.picture.path)
        if img.width > 400 and img.height > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.picture.path)

@receiver(pre_delete, sender=ContentPicture)
def picture_file_delete(sender, instance, **kwargs):
    if instance.picture:
        os.remove(instance.picture.path)

