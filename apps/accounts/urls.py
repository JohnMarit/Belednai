from django.urls import path
from .views import CustomLogoutView

urlpatterns = [
    # Other URL patterns
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]