from django.urls import path
from apps.core.views.category.views import *

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='update'),
    path('category/list/delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete'),
]
