from pyexpat import model
from attr import fields
from rest_framework import serializers
from testapp.models import Quiz

class quizSerializers(serializers.ModelSerializer):
    class Meta:
        model=Quiz
        fields="__all__"