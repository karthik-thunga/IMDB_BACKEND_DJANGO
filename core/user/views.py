from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets
from core.user.serializers import UserSerializer, RegistrationSerializer
from core.user.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token

# class UserViewSet(viewsets.ModelViewSet):
#     http_method_names = ('get', 'patch')
#     permission_classes = IsAuthenticated,
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         if self.request.user.is_superuser:
#             return User.objects.all()
#         return User.objects.exclude(is_superuser=True)

#     def get_object_by_public_id(self):
#         obj = User.objects.get_object_by_public_id(public_id=self.kwargs['pk'])
#         self.check_object_permissions(self.request, obj)
#         return obj

@api_view(['GET'])
def list_users(request):
    users_list = User.objects.all()
    serializer = UserSerializer(users_list, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register_user(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            token, created = Token.objects.get_or_create(user=account)
            data = {
                'username' : serializer.data['username'],
                'email' : serializer.data['email'],
                'token' : token.key
            }

            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout(request):
    if request.method == 'GET':
        logged_user = request.user
        token = Token.objects.get(user=logged_user)
        token.delete()
        return Response({'detail' : 'logged out successfully'}, status=status.HTTP_200_OK)

