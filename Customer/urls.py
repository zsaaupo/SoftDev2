from django.urls import path
from .views import sign_up, sign_in, verify_email, ApiSignUp, ApiOTPCheck, ApiLogIn, CustomarDetailsApi

urlpatterns = [
    path('join', sign_up),
    path('log_in', sign_in),
    path('verify_email/<str:OTP>/<str:user_name>/', verify_email),

    #API
    path('sign_up_api/', ApiSignUp.as_view()),
    path('OTP_check_api/', ApiOTPCheck.as_view()),
    path('login_api/', ApiLogIn.as_view()),
    path('about/<slug:slug>/', CustomarDetailsApi.as_view()),
]