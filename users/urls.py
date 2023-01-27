from django.urls import path

from users.views import RegisterView, LoginView, UserView, id_check

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('<int:pk>/', UserView.as_view()),

    # 함수형 뷰
    path('username/<str:username>/', id_check),
]
