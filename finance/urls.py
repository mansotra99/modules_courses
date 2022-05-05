from django.urls import path
from .views import *
urlpatterns = [
    path('get-modeules/',GetModulesView.as_view()),
    path('get-chapters/',GetChaptersView.as_view()),
    path('get-header-details/',HeaderDetailsView.as_view()),
    path('get-questions/',GetQuestionsView.as_view()),
    path('verify-answers/',VerifyAnswersView.as_view()),
    
]