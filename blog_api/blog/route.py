from .views import CommentViewSet,PostViewSet

from django.urls import include,path

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('posts',PostViewSet)
router.register('comments',CommentViewSet)

urlpatterns=[
    path('',include(router.urls))
]