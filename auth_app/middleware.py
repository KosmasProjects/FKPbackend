# my_app/middleware.py

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model

class TokenAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.headers.get('Authorization')
        if token:
            User = get_user_model()
            for user in User.objects.all():
                if PasswordResetTokenGenerator().check_token(user, token):
                    request.user = user
                    break
        return self.get_response(request)