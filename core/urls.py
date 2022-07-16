from django.urls import path, include
from rest_framework_nested import routers
from core.views import *

router = routers.DefaultRouter()
router.register(r'surveys', SurveyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', CreateSurveyView.as_view(), name='create'),
    path('create/question/', CreateQuestionView.as_view(), name='create_question'),
    path('create/question/choice/', CreateChoiceView.as_view(), name='create_choice'),
]
