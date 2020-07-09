from django.shortcuts import HttpResponseRedirect, redirect, reverse
from django.contrib.sessions.models import Session


#Custom Middleware for authentication
class AuthRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_request(self, request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('UploadApp:login'))
        return None
