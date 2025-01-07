from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import UpdateView
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from api.serializers import (CusomerSerializer, QuestionSerializer,
                             QuizSerializer)
from core.permissions import IsSuperUser
from quiz.models import Question, Quiz


class CustomerViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CusomerSerializer


class QuestionDetailView(RetrieveAPIView):
    serializer_class = QuestionSerializer

    def get_object(self):
        return Question.objects.get(quiz__pk=self.kwargs.get("pk"), order_number=self.kwargs.get("order"))


class QuizListView(ListAPIView):
    permission_classes = [AllowAny | IsSuperUser]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizCreateView(CreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizUpdateView(UpdateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizDeleteView(DestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
