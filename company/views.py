from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from company.models import Company
from company.serializers import CompanySerializer


# Create your views here.
class CompanyView(APIView):
    def post(self, request):
        serializer = CompanySerializer(data=request.data)

        # 사업자 등록 번호 '-' 체크
        if '-' in serializer.initial_data['business_number']:
            return Response({'message': "사업자 등록 번호는 '-' 없이 입력해주시기 바랍니다"}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        company = get_object_or_404(Company, pk=pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, pk):
        company = get_object_or_404(Company, pk=pk)

        if not request.user.is_authenticated:
            return Response({'message': 'Token needed'}, status=status.HTTP_401_UNAUTHORIZED)

        if request.user.type != 'manager' or request.user.company != company:
            return Response({'message': 'You are not a manager'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = CompanySerializer(company, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
