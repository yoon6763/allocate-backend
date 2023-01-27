from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .models import User


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data

        return Response({"token": token.key}, status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name='dispatch')
class UserView(APIView):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)

        return Response(serializer.data)

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)

        # check '-' in phone_number
        if '-' in serializer.initial_data['phone_number']:
            return Response({'message': "전화번호는 '-' 없이 입력해주시기 바랍니다"}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# id duplicate check
@api_view(["GET"])
def id_check(request, username):
    if User.objects.filter(username=username).exists():
        return Response({'message': '이미 사용중인 아이디 입니다'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': '사용 가능한 아이디 입니다'}, status=status.HTTP_200_OK)
