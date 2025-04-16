from django.urls import path
from .views import UserCreateView, UserLoginView, UserUpdateAPIView


urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),

    path('user-update/', UserUpdateAPIView.as_view(), name='user-update'),
]