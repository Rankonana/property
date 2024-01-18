from django.shortcuts import render, get_object_or_404
# from .models import House


def home(request):
    # houses = house.objects.all()
    return render(request, 'base/home.html', {'houses': "houses"})


def add_house(request, pk):
    # house = get_object_or_404(house, pk=pk)
    return render(request, 'base/add_house.html', {'house': "house"})

def house_list(request):
    # houses = house.objects.all()
    return render(request, 'base/house_list.html', {'houses': "houses"})

def house_detail(request, pk):
    # house = get_object_or_404(house, pk=pk)
    return render(request, 'base/house_detail.html', {'house': "house"})



