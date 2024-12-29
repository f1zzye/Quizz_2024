from email.policy import default

from quiz.models import Category, Question, Quiz


def sample_quiz(title: str, **params) -> Quiz:
    defaults = {
        "description": "Test description",
        "category": Category.objects.create(),
    }
    defaults.update(params)
    return Quiz.objects.create(title=title, **defaults)


def sample_question(quiz: Quiz, order_number, **params) -> Question:
    defaults = {"text": "Test question"}
    defaults.update(params)
    return quiz.questions.create(quiz=quiz, order_number=order_number, **defaults)
