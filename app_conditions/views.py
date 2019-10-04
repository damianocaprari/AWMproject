from rest_framework import viewsets
from .serializers import ConditionSerializer
from .models import Condition

class ConditionViewSet(viewsets.ModelViewSet):
    serializer_class = ConditionSerializer
    queryset = Condition.objects.all()



#from django.shortcuts import render
#from app_conditions.models import Condition

#####
# from django.http import HttpResponse
####


def index(request):
    conditions = Condition.objects.all()
    context = {
        'conditions': conditions,
    }
    return render(request, 'app_conditions/list.html', context)


#def index(request):
#    return HttpResponse("Hello, page of CONDITIONS.")
