from rest_framework import serializers

from .models import Benefactor
from .models import Charity, Task


class BenefactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefactor
        fields = ('experience','free_time_per_week')
        
    def create(self, validated_data):
        benefactor = Benefactor(**validated_data)

        benefactor.save()
        return benefactor

class CharitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Charity
        fields = ('name','reg_number')
        
    def create(self, validated_data):
        charity = Charity(**validated_data)

        charity.save()
        return charity



class TaskSerializer(serializers.ModelSerializer):
    pass