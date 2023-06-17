from django.urls import path
from .views import TodoCreateView, TodoUpdateView, TodoDeleteView,TodoReadView

urlpatterns = [
    path('api/todo/all/', TodoReadView.as_view(), name='todo-read'),
    path('api/todo/create/', TodoCreateView.as_view(), name='todo-create'),
    path('api/todo/update/<int:pk>/', TodoUpdateView.as_view(), name='todo-update'),
    path('api/todo/delete/<int:pk>/', TodoDeleteView.as_view(), name='todo-delete'),
]
