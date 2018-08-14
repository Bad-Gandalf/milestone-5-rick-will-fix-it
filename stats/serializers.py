from rest_framework import serializers
from .models import BugWorkTime
from bugs.models import Post


class BugWorkTimeSerializer(serializers.ModelSerializer):
    bug = serializers.SlugRelatedField(read_only=True, slug_field='title')
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = BugWorkTime
        fields = ('time_spent_mins', 'timestamp', 'bug', 'user')
        
    