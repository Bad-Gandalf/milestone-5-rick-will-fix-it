#from djqscsv import render_to_csv_response
#from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.core import serializers
from .models import BugWorkTime
#from django.views.generic import View
#from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BugWorkTimeSerializer



# Create your views here.

class BugWorkTimeList(APIView):
    
    def get(self, request):
        bugworktimes = BugWorkTime.objects.all()
        serializer = BugWorkTimeSerializer(bugworktimes, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass
        
