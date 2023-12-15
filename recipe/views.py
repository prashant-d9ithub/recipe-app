from django.shortcuts import render
import requests
import json

# Create your views here.
def RecipePage(request):
    return render(request,'recipe/recipe.html')

def RandomMeal(request):
    api_url = "https://www.themealdb.com/api/json/v1/1/random.php"
    response = requests.get(api_url)

    if response.status_code == 200:
        api_data = response.json()
        meal = api_data.get('meals',[])
        Name = meal[0].get('strMeal')
        Drink = meal[0].get('strDrinkAlternate')
        Category = meal[0].get('strCategory')
        Area = meal[0].get('strArea')
        Instruction = meal[0].get('strInstructions')
        Thumb = meal[0].get('strMealThumb')
        Tags = meal[0].get('strTags')
        Youtube = meal[0].get('strYoutube')
        Ingredients = []
        Measure = []
        for i in range(1,21):
            Ing = meal[0].get('strIngredient'+str(i))
            Ingredients.append(Ing)
            Msure = meal[0].get('strMeasure'+str(i))
            Measure.append(Msure)
        mylist = zip(Ingredients, Measure)
    context = {"Name":Name,"Drink":Drink,"Category":Category,"Area":Area,"Instruction":Instruction,"Thumb":Thumb,"Tags":Tags,"Youtube":Youtube,'mylist': mylist,}

    return render(request,'recipe/meals.html',context)
