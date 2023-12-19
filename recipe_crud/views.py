from django.shortcuts import render,HttpResponseRedirect
from .forms import RecipeAdd
from .models import Recipe
# Create your views here.


# Create and Show
def crud(request):
    if request.method == "POST":
        fm = RecipeAdd(request.POST)
        if fm.is_valid():
            rn = fm.cleaned_data['rname']
            rc = fm.cleaned_data['rcategory']
            ra = fm.cleaned_data['rarea']
            rd = fm.cleaned_data['rdrink']
            ri = fm.cleaned_data['rinstruction']
            rv = fm.cleaned_data['rvideoLink']
            reg = Recipe(rname=rn,rcategory=rc,rarea=ra,rdrink=rd,rinstruction=ri,rvideoLink=rv)
            reg.save()
            fm = RecipeAdd()
    else :
        fm = RecipeAdd()
    recipe = Recipe.objects.all()
    return render(request,'crud/home_crud.html',{'form':fm,'recipe':recipe})

# ! Delete Recipe
def deleteRecipe(request,id):
    if request.method == "POST":
        pi = Recipe.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/crud/')

# ! Update Recipe
def updateRecipe(request,id):
    if request.method == "POST":
        pi = Recipe.objects.get(pk=id)
        fm = RecipeAdd(request.POST,instance=pi)
        if fm.is_valid():
            rn = fm.cleaned_data['rname']
            rc = fm.cleaned_data['rcategory']
            ra = fm.cleaned_data['rarea']
            rd = fm.cleaned_data['rdrink']
            ri = fm.cleaned_data['rinstruction']
            rv = fm.cleaned_data['rvideoLink']
            reg = Recipe(rname=rn,rcategory=rc,rarea=ra,rdrink=rd,rinstruction=ri,rvideoLink=rv)
            reg.save()
    else:
        
        pi = Recipe.objects.get(pk=id)
        fm = RecipeAdd(instance=pi)

    return render(request,"crud/update.html",{'form':fm})
