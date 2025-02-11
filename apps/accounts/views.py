from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(never_cache, name='dispatch')
class CustomLogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')  # Redirect to the login page or any other page