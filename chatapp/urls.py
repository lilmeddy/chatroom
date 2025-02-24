from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("signup/", signup, name="signup"),
    path("login/", signin, name="login"),
    path("logout/", logoutUser, name="logout"),
    path("profile/<str:pk>/", profile, name="profile"),
    path("settings/<str:pk>/", settings, name="settings"),
    path("create-room/", createRoom, name="create-room"),
    path("roomdetails/<str:pk>/", roomDetails, name="roomdetails"),
    path("edit/<str:pk>/", editDetails, name="edit"),
    path("delete/<str:pk>/", deleteRoom, name="delete"),
    path("notifications", notifications, name="notifications"),
    path("chatbot", chatbot, name="chatbot"),
    path("chat/<str:pk>/", chatbotId, name="chat")
    # path('chat/<int:room_id>/', chatbot, name='chatbot'),
]