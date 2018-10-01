from django.shortcuts import render
from django.core import serializers
from .models import BugWorkTime
from bugs.models import Post
from features.models import Feature
from checkout.models import OrderLineItem
from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (BugWorkTimeSerializer, PostSerializer,
OrderLineItemSerializer, FeatureSerializer)

"""Will render pages for site statistics. javascript files will use d3 to
create the charts."""


def display_stats(request):
    return render(request, 'stats/workflow.html')


def display_upvotes(request):
    return render(request, 'stats/bugs_by_upvotes.html')


def display_feature_stats(request):
    return render(request, 'stats/feature_stats.html')


"""The below classes create the api views with the json data in order for the
d3/javascript files to parse the data and create the appropriate charts."""


class BugWorkTimeListDaily(APIView):
    """If statements to adjust for last working day i.e Friday when the
    user checks on a Sunday or Monday"""
    def get(self, request):
        today = datetime.today()
        if datetime.today().isoweekday() == 7:  # Sunday
            yesterday = today - timedelta(days=2)
        elif datetime.today().isoweekday() == 1:  # Monday
            yesterday = today - timedelta(days=3)
        else:
            yesterday = today - timedelta(days=1)
        qs = BugWorkTime.objects.filter(timestamp__gte=yesterday)
        serializer = BugWorkTimeSerializer(qs, many=True)
        return Response(serializer.data)


class BugWorkTimeListWeekly(APIView):
    """Provides a json for work spent on each bug in the last 7 days"""
    def get(self, request):
        today = datetime.today()
        week = today - timedelta(days=7)
        qs = BugWorkTime.objects.filter(timestamp__gte=week)
        serializer = BugWorkTimeSerializer(qs, many=True)
        return Response(serializer.data)


class BugWorkTimeListMonthly(APIView):
    """Provides a json for work spent on each bug in the last 31 days"""
    def get(self, request):
        today = datetime.today()
        month = today - timedelta(days=31)
        qs = BugWorkTime.objects.filter(timestamp__gte=month)
        serializer = BugWorkTimeSerializer(qs, many=True)
        return Response(serializer.data)


class CurrentBugUpvotes(APIView):
    """Provides a json for upvotes on working bugs"""
    def get(self, request):
        qs = Post.objects.filter(status=2)
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)


class OpenBugUpvotes(APIView):
    """Provides a json for upvotes on open bugs"""
    def get(self, request):
        qs = Post.objects.filter(status=1)
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)


class OpenFeaturesContributions(APIView):
    """Provides a json for total contributions to a particular feature."""
    def get(self, request):
        qs = Feature.objects.filter(status=2)
        serializer = FeatureSerializer(qs, many=True)
        return Response(serializer.data)
