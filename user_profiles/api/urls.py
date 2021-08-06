from django.urls import path
from user_profiles.api import views as api_views

urlpatterns = [
    path('detail/<int:pk>/', api_views.UserProfileDetail.as_view(), name='user_profile')
]
