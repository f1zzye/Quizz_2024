from django.contrib.auth import get_user, get_user_model
from django.core.validators import MaxValueValidator
from django.db import models

from core.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.id})"


class Quiz(BaseModel):
    QUESTION_MAX_LIMIT = 20

    class LEVEL_CHOICES(models.IntegerChoices):
        BASIC = 0, "Basic"
        MIDDLE = 1, "Middle"
        ADVANCED = 2, "Advanced"

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1024, blank=True, null=True)
    image = models.ImageField(default="default.png", upload_to="covers")
    category = models.ForeignKey(to="quiz.Category", related_name="quizzes", on_delete=models.CASCADE)
    level = models.IntegerField(choices=LEVEL_CHOICES.choices, default=LEVEL_CHOICES.BASIC)

    def __str__(self):
        return f"{self.title} ({self.id})"

    def questions_count(self):
        return self.questions.count()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Results(BaseModel):
    quiz = models.ForeignKey(to="quiz.Quiz", related_name="results", on_delete=models.CASCADE)
    user = models.ForeignKey(to=get_user_model(), related_name="results", on_delete=models.CASCADE)


class Question(BaseModel):
    quiz = models.ForeignKey(to="quiz.Quiz", related_name="questions", on_delete=models.CASCADE)
    order_number = models.PositiveIntegerField(validators=[MaxValueValidator(limit_value=Quiz.QUESTION_MAX_LIMIT)])
    text = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.text} ({self.order_number})"


class Choice(BaseModel):
    question = models.ForeignKey(to="quiz.Question", related_name="choices", on_delete=models.CASCADE)
    text = models.CharField(max_length=120)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({self.question.order_number})"
