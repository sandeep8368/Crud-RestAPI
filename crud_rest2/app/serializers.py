from app.models import StudentModel
from rest_framework import serializers


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'