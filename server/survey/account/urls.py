from django.urls import path, include
from .views import *

urlpatterns = [
    path('users/', GetUserList.as_view()),
    path('users/<int:pk>', GetUserDetail.as_view()),
    path('users/create', CreateUser.as_view()),
    path('users/update/<int:pk>', UpdateUser.as_view())
]
