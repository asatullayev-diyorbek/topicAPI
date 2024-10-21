from django.urls import path

from . import views

app_name = 'topic'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),


    path('generic/topic/list/', views.TopicListGenericView.as_view(), name="generic-topic-list"),
    path('generic/topic/<int:pk>/detail/', views.TopicDetailGenericView.as_view(), name="generic-topic-detail"),

    path('topic/list/', views.TopicListView.as_view(), name="topic-list"),
    path('topic/<int:pk>/detail/', views.TopicDetailView.as_view(), name="topic-detail"),

    path('comment/list/', views.CommentListView.as_view(), name="comment-list"),
    path('comment/<int:pk>/detail/', views.CommentDetailView.as_view(), name="comment-detail"),
]
