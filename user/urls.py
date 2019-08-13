from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from user import views

app_name = 'user'

urlpatterns = [
	path('login',LoginView.as_view(),name='login'),
	path('logout',LogoutView.as_view(),name='logout'),
	path('register',views.RegisterView.as_view(),name='register'),
]
