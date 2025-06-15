from django.urls import path
from .views import (
    RecordListView, 
    RecordCreateView, 
    RecordDetailView, 
    LikeView, 
    CommentCreateView
)

app_name = 'records'

urlpatterns = [
    path('', RecordListView.as_view(), name='record_list'),
    path('create/', RecordCreateView.as_view(), name='record_create'),
    path('record/<int:pk>/', RecordDetailView.as_view(), name='record_detail'),
    path('record/<int:pk>/like/', LikeView.as_view(), name='like'),
    path('record/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
]
