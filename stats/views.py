#from djqscsv import render_to_csv_response
#from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.core import serializers
from .models import BugWorkTime
from bugs.models import Post
from features.models import Feature
from checkout.models import OrderLineItem
from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BugWorkTimeSerializer, PostSerializer, OrderLineItemSerializer, FeatureSerializer

# Create your views here.
def display_stats(request):
    return render(request, 'stats/workflow.html')
    
def display_upvotes(request):
    return render(request, 'stats/bugs_by_upvotes.html')
    
def display_feature_stats(request):
    return render(request, 'stats/feature_stats.html')
    
    

class BugWorkTimeListDaily(APIView):
    # If statements to adjust for last working day i.e Friday when the 
    # user checks on a Sunday or Monday
    def get(self, request):
        today = datetime.today()
        if datetime.today().isoweekday() == 7: #Sunday
            yesterday = today - timedelta(days=2)
        elif datetime.today().isoweekday() == 1:
            yesterday = today - timedelta(days=3) #Monday
        else:
            yesterday = today - timedelta(days=1)
        qs = BugWorkTime.objects.filter(timestamp__gte=yesterday)
        serializer = BugWorkTimeSerializer(qs, many=True)
        return Response(serializer.data)
    
    
        
class BugWorkTimeListWeekly(APIView):
    def get(self, request):
        today = datetime.today()
        week = today - timedelta(days=7)
        qs = BugWorkTime.objects.filter(timestamp__gte=week)
        serializer = BugWorkTimeSerializer(qs, many=True)
        return Response(serializer.data)
    
    
    
class BugWorkTimeListMonthly(APIView):
    
    def get(self, request):
        today = datetime.today()
        month = today - timedelta(days=31)
        qs = BugWorkTime.objects.filter(timestamp__gte=month)
        serializer = BugWorkTimeSerializer(qs, many=True)
        return Response(serializer.data)
    
    
    
class CurrentBugUpvotes(APIView):
    
    def get(self, request):
        qs = Post.objects.filter(status=2)
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)
        
class OpenBugUpvotes(APIView):
    
    def get(self, request):
        qs = Post.objects.filter(status=1)
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)
        
class OpenFeaturesContributions(APIView):
    def get(self, request):
        qs = Feature.objects.filter(status=2)
        serializer = FeatureSerializer(qs, many=True)
        return Response(serializer.data)
    