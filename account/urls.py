from django.urls import path
from .views import userRegistration, activate, userLogin, UserLogOut

urlpatterns = [
    path('register/', userRegistration.as_view(), name='user-registration'),
    path('active/<uid64>/<token>', activate, name='activation'),
    path('login/', userLogin.as_view(), name='login'),
    path('logout/<int:id>/<token>', UserLogOut, name='logout'),
    
]
