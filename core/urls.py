from django.urls import path
from core.user.views import list_users
from core.watch_it.views import (ContentViewAV, ContentDetailViewAV,
                                StreamPlatformViewAV, StreamPlatformDetailViewAV,
                                ReviewView, ReviewCreate, ReviewDetailView, ContentPictureDetailView)

urlpatterns = [
    path('users/', list_users, name='list-users'),
    path('content/', ContentViewAV.as_view(), name='list-content'),
    path('content/<int:pk>', ContentDetailViewAV.as_view(), name='content-detail'),
    path('content/<int:pk>/review/', ReviewView.as_view(), name='list-review'),
    path('content/<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('content/review/<int:pk>', ReviewDetailView.as_view(), name='review-detail'),
    path('stream/', StreamPlatformViewAV.as_view(), name='list-stream'),
    path('stream/<int:pk>/', StreamPlatformDetailViewAV.as_view(), name='platform-detail'),
    path('content/picture/<int:pk>', ContentPictureDetailView.as_view(), name='picture-detail'),
]
