import os
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from .models import *
from .serializers import *

#AFRICASTALKING
import africastalking
username = os.environ.get('AFRICASTALKING_USERNAME')
api_key = os.environ.get('AFRICASTALKING_API_KEY')
africastalking.initialize(username, api_key)  
sms = africastalking.SMS

##Send Email
import smtplib
from django.core.mail import send_mail 

# Create your views here.

@api_view(['POST'])
def feedback(request):
    name = request.data.get('name')
    email = request.data.get('email')
    serializer = PotentialEmployerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        phone_number = '+254717423651'
        recipient = [email]
        subject = 'Feedback for My Job Application'
        content = f'Dear {name},I am pleased to hear from you. Thank you for considering my application to be a part of your great team.'
        send_mail(subject, content,os.environ.get('EMAIL_HOST_USER1'),recipient, fail_silently=False) 
        sms.send(f'You have a message from a potential employer by the name of {name}',[f'{phone_number}'],callback=feedback)
        return Response(serializer.data)

class EmployerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = PotentialEmployer.objects.all()
    serializer_class = PotentialEmployerSerializer