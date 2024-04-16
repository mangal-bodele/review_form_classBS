from django.urls import path
from .views import Add_Review,Show_Review,Update_Review,Delete_Review

urlpatterns = [
    path('add/',Add_Review.as_view(),name='add_url'),
    path('show/',Show_Review.as_view(),name='show_url'),
    path('update/<int:pk>/',Update_Review.as_view(),name='update_url'),
    path('delete/<int:pk>/',Delete_Review.as_view(),name='delete_url')
]