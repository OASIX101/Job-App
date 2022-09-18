from django.urls import path, include
from . import views 

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('access/', include('djoser.urls.jwt')),
    path('logout/', views.logout_view),
    path('login/', views.login_view),
]