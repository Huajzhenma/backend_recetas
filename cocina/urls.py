from django.urls import path
from cocina import views


urlpatterns = [
    path('api/recetas/<int:id>/'
         , views.cocina_list),  
    path('api/recetas/'
     , views.cocina_list),    
]