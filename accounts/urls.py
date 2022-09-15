from django.urls import path, include
from . import views 

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('access/', include('djoser.urls.jwt')),
    path('login/', views.logout_view),
    path('logout/', views.login_view),
]