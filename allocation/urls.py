from django.urls import path

from allocation.views import AllocationView

urlpatterns = [
    path('', AllocationView.as_view()),
    path('<int:pk>/', AllocationView.as_view()),
]
