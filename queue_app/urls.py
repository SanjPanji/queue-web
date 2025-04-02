from django.urls import path
from . import views

urlpatterns = [
    path('root/', views.api_root_view, name="api_root_view"),
    path('queue/', views.get_full_queue, name='get_full_queue'),
    path('post/', views.post_queue, name='post_queue'),
    path('queue/detail/<int:pk>/', views.get_queue_view, name='get_queue_view'),
    path('queue/delete/<int:pk>/', views.delete_queue_self, name='delete_item_view'),
    path('reviews/post/', views.post_review, name='post_review')
]