from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict, name='predict'),
    path('history/', views.history, name='history'),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
]