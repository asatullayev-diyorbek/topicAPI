from django.urls import path

from . import views

app_name = 'topic'
urlpatterns = [
    path('topic/list/', views.TopicListView.as_view(), name="topic-list"),
    path('topic/<int:pk>/detail/', views.TopicDetailView.as_view(), name="topic-detail"),
]
