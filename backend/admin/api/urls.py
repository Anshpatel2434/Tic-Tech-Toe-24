from django.urls import path
from .views import *

urlpatterns = [
    path("user/signup", UserSignupView.as_view()),
    path("user/signin", UserSigninView.as_view()),
    path("user/getUser", GetUserView.as_view()),
    path("user/getUserById/<int:user_id>", GetUserByIdView.as_view()),
    path("user/setGender", SetGender.as_view()),

]