from django.urls import path

from company.views import CompanyView

urlpatterns = [
    path('', CompanyView.as_view()),
    path('<int:pk>/', CompanyView.as_view()),
]
