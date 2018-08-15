#from djqscsv import render_to_csv_response
#from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.core import serializers
from .models import BugWorkTime
#from django.views.generic import View
from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BugWorkTimeSerializer



# Create your views here.
def display_stats(request):
    return render(request, 'stats/workflow.html')
    


class BugWorkTimeListDaily(APIView):
    
    def get(self, request):
        today = datetime.today()
        yesterday = today - timedelta(days=1)
        qs = BugWorkTime.objects.filter(timestamp__gte=yesterday)
        serializer = BugWorkTimeSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass
        
class BugWorkTimeListWeekly(APIView):
    
    def get(self, request):
        today = datetime.today()
        week = today - timedelta(days=7)
        qs = BugWorkTime.objects.filter(timestamp__gte=week)
        serializer = BugWorkTimeSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass
    
class BugWorkTimeListMonthly(APIView):
    
    def get(self, request):
        today = datetime.today()
        month = today - timedelta(days=31)
        qs = BugWorkTime.objects.filter(timestamp__gte=month)
        serializer = BugWorkTimeSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass