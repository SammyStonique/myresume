from django.urls import path
from . import views

urlpatterns = [
    path('employer-feedback/', views.feedback, name='feedback'),
    path('employer-list/', views.EmployerList.as_view()),
    path('employer-details/<int:pk>/', views.EmployerDetails.as_view()),
]