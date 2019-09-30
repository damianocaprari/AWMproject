from django.shortcuts import render
from .models import Monster


def index(request):
    monsters = Monster.objects.all()
    context = {
        'monsters': monsters,
    }
    return render(request, 'app_monsters/list.html', context)
