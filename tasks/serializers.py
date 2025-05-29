from rest_framework import serializers


class TaskEnqueueSerializer(serializers.Serializer):
    param = serializers.CharField()
