from rest_framework import serializers
from .models import *

class PotentialEmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PotentialEmployer
        fields=['id','name','email','message','date']