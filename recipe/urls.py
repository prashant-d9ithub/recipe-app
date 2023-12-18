from django.urls import path
from .views import RecipePage,RandomMeal,NameMeal,LetterMeal,Meal,CategoryMeal,CategoryMealData

urlpatterns = [
    path('recipe/',RecipePage,name='recipe'),
    path('rmeal/',RandomMeal,name='random-meal'),
    path('rname/',NameMeal,name='name-meal'),
    path('rletter/',LetterMeal,name='letter-meal'),
    path('rletter/<str:letter>/',Meal,name='letter-one'),
    path('rcategory/',CategoryMeal,name='category-one'),
    path('rcategory/<str:category>/',CategoryMealData,name='categorys'),
]