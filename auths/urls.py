from django.urls import path
# from .views import user_login
from. import views



urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.user_login, name='login'),
    # path('logout/', views.logout_view, name='logout')
    
]
