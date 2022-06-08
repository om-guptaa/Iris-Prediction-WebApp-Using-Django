import imp
from unittest import result
from django.shortcuts import render
import pandas as pd
from django.http import JsonResponse

from .models import PredResults


def predict(request):
    return render(request, 'predict.html')


def predict_chances(request):

    # Receive data from client
    if request.POST.get('action') == 'post':
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))

        # Unpickle model
        model = pd.read_pickle(r"C:\Users\Om Gupta\Downloads\new_model.pickle")

        # Make prediction
        result = model.predict(
            [[sepal_length, sepal_width, petal_length, petal_width]])

        classification = result[0]

        # Making entry in database
        PredResults.objects.create(sepal_length=sepal_length,
                                   petal_length=petal_length,
                                   sepal_width=sepal_width,
                                   petal_width=petal_width,
                                   classification=classification)

        return JsonResponse({'result': classification, 'sepal_length': sepal_length,
                             'sepal_width': sepal_width, 'petal_length': petal_length, 'petal_width': petal_width},
                            safe=False)


def view_results(request):
    data = {"dataset": PredResults.objects.all()}
    return render(request, 'results.html', data)
