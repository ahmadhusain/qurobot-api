from rest_framework import serializers

from .models import Datamaster, ListDoa

class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = Datamaster
        # fields = '__all)__'
        fields = ('number', 'arab', 'indonesia', 'perawi')

class PerawiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datamaster
        # fields = '__all)__'
        fields = ['perawi']
        
class DoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListDoa
        fields = '__all__'