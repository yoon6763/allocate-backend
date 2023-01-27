from rest_framework import serializers

from allocation.models import Allocation


class AllocationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allocation
        fields = [
            'pk',
            'company_id',
            'client_name',
            'client_phone_number',
            'location_start',
            'location_end',
            'duration_start',
            'duration_end',
            'time_start',
            'status',
            'vehicle',
            'point',
        ]


class AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allocation
        fields = [
            'pk',
            'company_id',
            'employee_id',
            'client_name',
            'client_phone_number',
            'location_start',
            'location_end',
            'duration_start',
            'duration_end',
            'time_start',
            'status',
            'vehicle',
            'point',
        ]

# name = models.CharField(max_length=100)
# company_id = models.ManyToOneRel(Company, related_name='allocates')
# employee_id = models.ManyToOneRel(User, related_name='allocates')
# client_name = models.CharField(max_length=100)
# client_phone_number = models.CharField(max_length=100)
# location_start = models.CharField(max_length=100)
# location_end = models.CharField(max_length=100)
# duration_start = models.DateField()
# duration_end = models.DateField()
# time_start = models.TimeField()
# status = models.CharField(max_length=100)
# vehicle = models.FloatField(max_length=100)
# point = models.DecimalField()  # 돈과 관련된 것은 DecimalField 를 사용
