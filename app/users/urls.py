from django.urls import path

from users import views


app_name = 'users'

urlpatterns = [
    path('', views.CreateUserView.as_view(), name='create'),
    path('login/', views.LoginView.as_view(), name='login')
]
