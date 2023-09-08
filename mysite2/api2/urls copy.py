from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('post', PostViewSet)
router.register('comment', CommentViewSet)

urlpatterns = [
 path('', include(router.urls)),
]
