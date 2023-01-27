from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from allocation.models import Allocation
from allocation.serializers import AllocationCreateSerializer, AllocationSerializer


# Create your views here.
class AllocationView(APIView):
    def post(self, request):
        serializer = AllocationCreateSerializer(data=request.data)

        company_id = self.request.user.company_id

        if serializer.is_valid():
            serializer.save(company_id=company_id)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        allocation = get_object_or_404(Allocation, pk=pk)
        serializer = AllocationSerializer(allocation)
        return Response(serializer.data)
