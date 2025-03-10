from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from . import views  # Import your views

class CustomLoginView(auth_views.LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')  # Redirect to the dashboard if the user is authenticated
        return super().dispatch(request, *args, **kwargs)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', CustomLoginView.as_view(), name='login'),  # Use the custom login view
    path('dashboard/', views.dashboard, name='dashboard'),  # Add the dashboard URL pattern
    # ...existing code...
]
