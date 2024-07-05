import json
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


@csrf_exempt
def login_view(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                token_generator = PasswordResetTokenGenerator()
                token = token_generator.make_token(user)
                return JsonResponse({'message': 'Logged in successfully', 'token': token})
            else:
                return JsonResponse({'message': 'Invalid username or password'}, status=400)
        else:
            # Handle GET request
            return HttpResponse('Login page')
    except Exception as e:
        print("Exception:", str(e))
        return JsonResponse({'error': str(e)}, status=400)
    

@csrf_exempt
def list_users(request):
    print('tutaj jestem w list_users')
    if request.method == 'GET':
        User = get_user_model()
        users = User.objects.all().values('username', 'is_active')  # Query the User model
        return JsonResponse(list(users), safe=False)  # Return the users as JSON
    else:
        return HttpResponse('Method not allowed', status=405)