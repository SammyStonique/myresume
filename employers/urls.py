from django.urls import path
from . import views

urlpatterns = [
    path('employer-list/', views.feedback, name='feedback'),
    path('employer-details/<int:pk>/', views.EmployerDetails.as_view()),
]