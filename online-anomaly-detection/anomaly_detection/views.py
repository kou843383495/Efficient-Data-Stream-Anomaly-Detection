from django.http import JsonResponse
from django.shortcuts import render

from .generate_data import get_history_data
from .tools import default_weight


# Create your views here.


def index(request):
    return render(request, 'anomaly_detection/index.html')


def history_data(request):
    print(request.POST.getlist('data[]'))
    weight = request.POST.getlist('data[]')
    if len(weight) == 7:
        data = get_history_data(weight)
    else:
        data = get_history_data()
    history_y = data[0]
    history_x = data[1]
    color = data[2]
    return JsonResponse({'history_data': history_y,
                         'history_x': history_x,
                         'default_weight': default_weight,
                         'color': color}
                        )
