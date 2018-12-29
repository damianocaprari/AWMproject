from django.shortcuts import render
from app_spells.models import Spell


def index(request):
    spells = Spell.objects.order_by('level')
    context = {
        'spells': spells,
    }
    return render(request, 'app_spells/list.html', context)
