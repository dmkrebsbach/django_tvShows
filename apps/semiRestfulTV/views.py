from django.shortcuts import render, redirect
from django.contrib import messages


from .models import Show

def index(request):
    return redirect("/shows")

def showAll(request):
    showDict = {}
    showDict["shows"] = Show.objects.all()
    return render(request, "semiRestfulTV/allShows.html", showDict)

def new(request):
    return render(request, "semiRestfulTV/newShow.html")

def createShow(request):
    if request.method == "POST":

        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                
            return redirect(f'/shows/new')

        showNew = Show(
            title = request.POST["title"],
            network = request.POST["network"],
            releaseDate = request.POST["releaseDate"],
            description = request.POST["description"],
        )
        messages.success(request, "You sucessfully added this show to your database")
        showNew.save()

    return redirect(f"/shows/{showNew.id}")

def showDesc(request, showId):
    showSumDict = {}
    showSumDict["showInd"] = Show.objects.get(id=showId)
    return render(request, "semiRestfulTV/indShow.html", showSumDict)

def editShow(request, showId):
    showDict = {}
    showDict["showEdit"] = Show.objects.get(id = showId)
    return render(request, "semiRestfulTV/editShow.html", showDict)

def updateShow(request, showId):
    if request.method == "POST":

        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{showId}/edit')

        updateThisShow = Show.objects.get(id = showId)
        updateThisShow.title = request.POST["title"]
        updateThisShow.network = request.POST["network"]
        updateThisShow.releaseDate = request.POST["date"]
        updateThisShow.description = request.POST["description"]
        updateThisShow.save()

    messages.success(request, "You sucessfully updated this show in your database")  
    return redirect(f"/shows/{updateThisShow.id}")

def destroyShow(request, showId):
    deleteShow = Show.objects.get(id = showId)
    deleteShow.delete()
    return redirect(f"/shows")









