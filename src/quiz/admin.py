from django.contrib import admin

from quiz.models import Category, Choice, Question, Quiz, Results

admin.site.register([Quiz, Category, Question, Choice, Results])
