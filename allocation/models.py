from django.db import models

from company.models import Company
from users.models import User


# Create your models here.
class Allocation(models.Model):
    name = models.CharField(max_length=100)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='allocates')
    employee_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='allocates')
    client_name = models.CharField(max_length=100)
    client_phone_number = models.CharField(max_length=100)
    location_start = models.CharField(max_length=100)
    location_end = models.CharField(max_length=100)
    duration_start = models.DateField()
    duration_end = models.DateField()
    time_start = models.TimeField()
    status = models.CharField(max_length=100)
    vehicle = models.FloatField(max_length=100)

    # 돈과 관련된 것은 DecimalField 를 사용
    # max_digits는 총 자릿수, decimal_places는 소수점 자릿수 (decimal_places는 max_digits보다 작아야 함)
    point = models.DecimalField(max_digits=20, decimal_places=0)

    def __str__(self):
        return self.name
