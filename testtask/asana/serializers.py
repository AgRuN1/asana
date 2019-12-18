from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.Serializer):
	user = serializers.StringRelatedField()
	project = serializers.StringRelatedField()
	txt = serializers.CharField(required=True)