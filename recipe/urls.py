from django.urls import path
from .views import RecipePage,RandomMeal

urlpatterns = [
    path('recipe/',RecipePage,name='recipe'),
    path('rmeal/',RandomMeal,name='random-meal'),
]