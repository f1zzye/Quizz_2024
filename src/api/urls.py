from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions
from rest_framework.decorators import permission_classes

from api.views import (CustomerViewSet, QuestionDetailView, QuizCreateView,
                       QuizDeleteView, QuizListView, QuizUpdateView)

app_name = "api"
router = routers.DefaultRouter()
router.register("customers", CustomerViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Quiz API",
        default_version="v1",
        description="Api for passing questions",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="user@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
    ]
)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls.jwt")),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),

    path("quiz/<int:pk>/question/<int:order>", QuestionDetailView.as_view(), name="question-detail"),
    path("quiz/", QuizListView.as_view(), name="quiz-list"),
    path("quiz/create/", QuizCreateView.as_view(), name="quiz-create"),
    path("quiz/<int:pk>/update/", QuizUpdateView.as_view(), name="quiz-update"),
    path("quiz/<int:pk>/delete/", QuizDeleteView.as_view(), name="quiz-delete"),
]
