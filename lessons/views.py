from django.shortcuts import render
from lessons.models import Activity, Step
from rest_framework import viewsets
from lessons.serializers import ActivitySerializer, StepSerializer

# Create your views here.

class ActivityViewSet(viewsets.ModelViewSet):

	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer

class StepViewSet(viewsets.ModelViewSet):

	queryset = Step.objects.all()
	serializer_class = StepSerializer