from rest_framework import serializers

from .models import Datamaster

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