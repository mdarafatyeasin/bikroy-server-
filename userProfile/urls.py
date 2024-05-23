from django.urls import path
from .views import additionalProfileInfo, basicInfoViewset, UserProfileView, userAdds

urlpatterns = [
    path('basic_info/<int:id>/', basicInfoViewset.as_view()),
    path('additional_info/<int:id>/', additionalProfileInfo.as_view()),
    path('user_profile/<int:id>/', UserProfileView.as_view()),
    path('my-adds/<int:id>', userAdds)
]
