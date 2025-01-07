from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from account.models import Customer
from quiz.models import Choice, Question, Quiz


class CusomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email", "is_staff")


class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = ("id", "text", "is_correct")


class QuestionSerializer(ModelSerializer):
    choices = ChoiceSerializer(many=True, required=True)

    class Meta:
        model = Question
        fields = ("id", "order_number", "text", "choices")


class QuizSerializer(ModelSerializer):
    level = CharField(source="get_level_display", read_only=True)

    class Meta:
        model = Quiz
        fields = ("id", "title", "description", "category", "level", "questions_count")
