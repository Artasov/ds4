from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

from . import api_views
from .api_views import CommentViewSet, PostViewSet

# urlpatterns = [
    # path('comment_example/', api_views.comment_example),
    # path('comment-update/<int:pk>/',
    #      api_views.CommentAPIUpdate.as_view()),
# ]

# urlpatterns = [
#     path('example/', api_views.example),
#     path('comment-list-create/', api_views.CommentAPIListCreate.as_view()),
#     path('comment-crud/<int:pk>/', api_views.CommentAPIGetPutDelete.as_view()),
#     path('comment-crud/', api_views.CommentAPIGetPutDelete.as_view()),
# ]

# urlpatterns = [
#     path('comment-list/',
#          CommentViewSet.as_view({
#              'get': 'list',
#              'post': 'create'
#          })),
#     path('comment-list/<int:pk>/',
#          CommentViewSet.as_view({
#              'get': 'retrieve',
#              'put': 'update',
#              'patch': 'partial_update',
#              'delete': 'destroy'
#          })),
# ]

# comment_router = SimpleRouter()
# comment_router.register(r'comment', CommentViewSet)
# urlpatterns = [
#     path('', include(comment_router.urls)),
# ]

router = DefaultRouter()
router.register(r'comment', CommentViewSet)  # basename=
router.register(r'post', PostViewSet)
urlpatterns = [
    path('', include(router.urls)),
]