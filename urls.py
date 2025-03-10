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
    path('', CustomLoginView.as_view(template_name='login.html'), name='login'),  # Use the custom login view
    path('dashboard/', views.dashboard, name='dashboard'),  # Add the dashboard URL pattern
    # ...existing code...
]




def redirect_authenticated_user(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')  # Replace 'dashboard' with your desired route
        return view_func(request, *args, **kwargs)
    return wrapper

urlpatterns = [
    path('', redirect_authenticated_user(auth_views.LoginView.as_view(template_name='login.html')), name='login'),
    # Other routes
]