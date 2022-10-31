from django.shortcuts import render, redirect
from .models import Food, Consume
# Create your views here.


def index(request):
    print("im outside if")

    if request.method=='POST':
        food = request.POST.get('food_consumed')
        consume = Food.objects.get(name=food)
        user = request.user
        consume = Consume.objects.get_or_create(user=user, food_consumed=consume)
        # consume.save()
    foods = Food.objects.all()
    print("im in index")
    print(foods)

    # else:
    #     foods = Food.objects.all()
    #     print("im in else")
    consumed_food = Consume.objects.get(name=food)

    return render(request, 'myapp/index.html', {'foods': foods, 'consumed_food': consumed_food})


def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    return render(request, 'myapp/delete.html')