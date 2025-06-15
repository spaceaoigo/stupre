from django.urls import path
from .views import RecordListView, RecordCreateView

app_name = 'records'

urlpatterns = [
    path('', RecordListView.as_view(), name='record_list'),
    path('create/', RecordCreateView.as_view(), name='record_create'),
]from django.urls import path
from .views import RecordListView, RecordCreateView

app_name = 'records'

urlpatterns = [
    path('', RecordListView.as_view(), name='record_list'),
    path('create/', RecordCreateView.as_view(), name='record_create'),
]
