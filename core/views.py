from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from core.models import *
from core.serializers import *


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Survey.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CreateSurveyView(generics.CreateAPIView):
    serializer_class = CreateSurveySerializer
    permission_classes = [permissions.IsAuthenticated]

    class Meta:
        model = Survey
        fields = '__all__'


class CreateQuestionView(generics.CreateAPIView):
    serializer_class = CreateQuestionSerializer
    permissions_classes = [permissions.IsAuthenticated]

    class Meta:
        model = Question
        fields = '__all__'


class CreateChoiceView(generics.CreateAPIView):
    serializer_class = CreateChoiceSerializer
    permission_classes = (permissions.IsAuthenticated,)

    class Meta:
        model = Choice
        fields = '__all__'


class ContributeView(viewsets.ModelViewSet):
    serializer_class = CreateChoiceSerializer

    # permission_classes = (permissions.IsAuthenticated,)
