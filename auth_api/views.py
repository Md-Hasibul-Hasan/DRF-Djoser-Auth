from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
import requests

User = get_user_model()


class GoogleLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        access_token = request.data.get('access_token')

        if not access_token:
            return Response(
                {'error': 'access_token required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Google থেকে user info নাও
        google_response = requests.get(
            'https://www.googleapis.com/oauth2/v3/userinfo',
            headers={'Authorization': f'Bearer {access_token}'}
        )

        if google_response.status_code != 200:
            return Response(
                {'error': 'Invalid Google token'},
                status=status.HTTP_400_BAD_REQUEST
            )

        google_data = google_response.json()
        email = google_data.get('email')
        name = google_data.get('name', '')

        if not email:
            return Response(
                {'error': 'Google account does not have email'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # User খোঁজো অথবা তৈরি করো
        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                'name': name,
                'is_active': True,
            }
        )

        if not created and not user.is_active:
            user.is_active = True
            user.save()

        # simplejwt দিয়ে token বানাও — exactly same format
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)