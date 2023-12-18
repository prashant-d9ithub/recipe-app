from django.urls import path
from .views import crud,deleteRecipe,updateRecipe

urlpatterns = [
    path('crud/',crud,name='crud'),
    path('delete/<int:id>/',deleteRecipe,name='deleterecipe'),
    path('update/<int:id>/',updateRecipe,name='updaterecipe'),
]