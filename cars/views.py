from django.shortcuts import render
from cars.models import Car


# fmt: off
def cars_view(request):
    # cars = Car.objects.all() #filtrar tudo
    cars = Car.objects.filter(model__contains='Chevette')

    return render(
        request,
        "cars.html",
        {"cars": cars}
    )
# fmt: on
