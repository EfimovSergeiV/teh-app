from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class AuthView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        print(f'\nreturn token: {type(token)}\n')
        return Response({"token": str(token) })

    
class UserView(APIView):

    def get(self, request):
        print(f'\nrequest.headers\n{request.headers}')

        try:
            print(request.user)
            user = request.user
            profile = User.objects.get(username=user)

            user = f'{ profile.first_name } { profile.last_name }'
            username = user if len(user) > 1 else profile.username

            return Response({
                'id': profile.id,
                'user': username,
                'first_name': profile.first_name,
                'last_name': profile.last_name,
                'email': profile.email,
            })
        except:
            return Response({"err": "User.DoesNotExist"})