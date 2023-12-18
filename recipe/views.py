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
def NameMeal(request):
    all_meals = []
    if request.method == "POST":
        value = request.POST.get('recipe') 
        if value is not None:
            all_meals = []
            api_url = "https://www.themealdb.com/api/json/v1/1/search.php?s="+str(value)
            response = requests.get(api_url)
            if response and response.status_code == 200:
                api_data = response.json()
                meals = api_data.get('meals',[])
                for i in meals:
                    Name = i.get('strMeal')
                    Drink = i.get('strDrinkAlternate')
                    Category = i.get('strCategory')
                    Area = i.get('strArea')
                    Instruction = i.get('strInstructions')
                    Thumb = i.get('strMealThumb')
                    Tags = i.get('strTags')
                    Youtube = i.get('strYoutube')
                    Ingredients = []
                    Measure = []
                    for j in range(1,21):
                        Ing = i.get('strIngredient'+str(j))
                        Ingredients.append(Ing)
                        Msure = i.get('strMeasure'+str(j))
                        Measure.append(Msure)
                    mylist = zip(Ingredients, Measure)
                    context = {"Name":Name,"Drink":Drink,"Category":Category,"Area":Area,"Instruction":Instruction,"Thumb":Thumb,"Tags":Tags,"Youtube":Youtube,'mylist': mylist}
                    all_meals.append(context)
            else:
                print('NO response come')
        else:
            print('Search Recipe')
    return render(request, 'recipe/name.html', {"all_meals": all_meals})


def LetterMeal(request):
    return render(request,'recipe/letter.html')

def Meal(request,letter):
    all_meals = []
    api_url = 'https://www.themealdb.com/api/json/v1/1/search.php?f='+str(letter)
    response = requests.get(api_url)
    if response and response.status_code == 200:
        all_meals = []
        api_data = response.json()
        meals = api_data.get('meals',[])
        if meals:
            for i in meals:
                Name = i.get('strMeal')
                Drink = i.get('strDrinkAlternate')
                Category = i.get('strCategory')
                Area = i.get('strArea')
                Instruction = i.get('strInstructions')
                Thumb = i.get('strMealThumb')
                Tags = i.get('strTags')
                Youtube = i.get('strYoutube')
                Ingredients = []
                Measure = []
                    
                for j in range(1,21):
                    Ing = i.get('strIngredient'+str(j))
                    Ingredients.append(Ing)
                    Msure = i.get('strMeasure'+str(j))
                    Measure.append(Msure)
                mylist = zip(Ingredients, Measure)
                context = {"Name":Name,"Drink":Drink,"Category":Category,"Area":Area,"Instruction":Instruction,"Thumb":Thumb,"Tags":Tags,"Youtube":Youtube,'mylist': mylist}
                all_meals.append(context)
            print(all_meals)
        else:
            print('NO Data for this letter')
    else:
        print('NO response come')
    return render(request,'recipe/meal.html',{"all_meals":all_meals})

def CategoryMeal(request):
    api_url = 'https://www.themealdb.com/api/json/v1/1/list.php?c=list'
    response = requests.get(api_url)
    if response and response.status_code == 200:
        api_data = response.json()
        categorys = api_data.get('meals',[])

    return render(request,'recipe/category.html',{'categorys':categorys})

def CategoryMealData(request,category):
    all_meals = []
    api_url = 'https://www.themealdb.com/api/json/v1/1/filter.php?c='+str(category)
    response = requests.get(api_url)
    if response and response.status_code == 200:
        all_meals = []
        api_data = response.json()
        meals = api_data.get('meals',[])
        if meals:
            for i in meals:
                Name = i.get('strMeal')
                Thumb = i.get('strMealThumb')
                context = {"Name":Name,"Thumb":Thumb}
                all_meals.append(context)
            print(all_meals)
        else:
            print('NO Data for this letter')
    else:
        print('NO response come')

    return render(request,'recipe/categoryMeal.html',{"all_meals":all_meals})

