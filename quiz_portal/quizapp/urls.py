from django.urls import path
from . import views


urlpatterns = [
path('login/', views.login_view, name='login'),
path('', views.register_view, name='register'),
path('dashboard/', views.dashboard, name='dashboard'),
path('quiz/', views.quiz_view, name='quiz'),
path('result/', views.result_view, name='result'),
path('logout/', views.logout_view, name='logout'),
]