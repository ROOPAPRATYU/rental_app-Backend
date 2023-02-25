from rest_framework import serializers
from accounts.serializers import OwnerSerializer
from .models import PropertyDetail,property_to_excel
from accounts.models import User


class ProperySerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyDetail
        exclude='owner',
    
class CurrentUserPropertySerialzer(serializers.ModelSerializer):
    property = ProperySerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'property']

class exporttoexcel(serializers.ModelSerializer):
    class Meta:
        model=PropertyDetail
        exclude="adhar_pic","property_pic","owner"
    
class ImportSerializer(serializers.ModelSerializer):
    class Meta:
        model=property_to_excel
        fields="__all__"



