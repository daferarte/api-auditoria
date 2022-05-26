from django.urls import path
from .views import *

urlpatterns = [
    path('v1/aud', AudSoft_APYView.as_view()),
    path('v1/aud/<int:pk>', AudSoft_APIView_Detail.as_view()),
]