from .models import TodoList
from rest_framework import serializers


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoList  # 통신할 모델
        fields = ('no', 'title', 'content', 'is_complete', 'end_date', 'priority')