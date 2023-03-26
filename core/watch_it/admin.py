from django.contrib import admin
from core.watch_it.models import Content, StreamPlatform, Review, ContentPicture
# Register your models here.
admin.site.register(Content)
admin.site.register(StreamPlatform)
admin.site.register(Review)
admin.site.register(ContentPicture)
