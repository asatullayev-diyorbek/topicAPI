from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Topic, Comment


class TopicSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    class Meta:
        model = Topic
        fields = '__all__'
