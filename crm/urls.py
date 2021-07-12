from django.urls import path

from crm import views

app_name = 'crm'

urlpatterns = [
    path('service/new/', views.CreateService.as_view(), name='new_service'),
]
