from django.urls import URLPattern,path
from  . import views


urlpatterns = [
    path('home',views.HomeView.as_view(), name='home'),
    path('authorized', views.AuthorizeView.as_view()),
]