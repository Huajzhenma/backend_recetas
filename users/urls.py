from django.urls import path
from cocina import views


urlpatterns = [
    path('api/users/<int:id>/'
         , views.cocina_list),  
    path('api/users/'
     , views.cocina_list),    
]
