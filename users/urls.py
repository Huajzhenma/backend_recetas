from django.urls import path
from users import views


urlpatterns = [
    path('api/users/<int:id>/'
         , views.users_list),  
    path('api/users/'
     , views.users_list),    
]
