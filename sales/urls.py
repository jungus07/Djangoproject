from django.urls import path
from .views import 세일목록,세일상세,세일입력

app_name = "홈페이지(homepage)"

urlpatterns = [
    path('',세일목록),
    path('<int:pk>/',세일상세),#컴퓨터는 위에서 아래로 컴파일하기때문에 이제부터 숫자로 인식
    path('make/',세일입력)
]