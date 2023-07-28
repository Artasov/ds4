from django.urls import path
from . import api_views


urlpatterns = [
    path('comment_example/', api_views.comment_example),
    # path('comment-list-create/', api_views.CommentAPIListCreate.as_view()),
    # path('comment-list-create/<int:pk>/', api_views.CommentAPIGetPutDelete.as_view()),
    # path('comment-list-create/', api_views.CommentAPIGetPutDelete.as_view()),
    # path('comment-update/<int:pk>/', api_views.CommentAPIUpdate.as_view()),
]
