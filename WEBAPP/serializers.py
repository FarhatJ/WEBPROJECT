from rest_framework import serializers
from . models import employees


class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = employees
        # fields = ('f_name', 'l_name')
        fields = '__all__'

