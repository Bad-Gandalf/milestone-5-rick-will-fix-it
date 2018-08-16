from rest_framework import serializers
from .models import BugWorkTime
from bugs.models import Post
from features.models import Feature
from checkout.models import OrderLineItem


class BugWorkTimeSerializer(serializers.ModelSerializer):
    bug = serializers.SlugRelatedField(read_only=True, slug_field='title')
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = BugWorkTime
        fields = ('time_spent_mins', 'timestamp', 'bug', 'user')
        


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'created_date', 'total_upvotes')
        
class OrderLineItemSerializer(serializers.ModelSerializer):
    feature = serializers.SlugRelatedField(read_only=True, slug_field='title')
    class Meta:
         
        model = OrderLineItem
        fields = ('feature','contribution',)

class FeatureSerializer(serializers.ModelSerializer):
    contributions = serializers.SlugRelatedField(read_only=True, many=True, slug_field='contribution')
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = Feature
        fields = ('title', 'author', 'price', 'contributions')
        
    