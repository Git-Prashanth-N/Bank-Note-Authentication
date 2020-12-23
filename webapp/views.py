# Create your views here.
from django.shortcuts import render
import pandas as pd
import numpy as np
import pickle
from django.views.generic import TemplateView

# Extracting pickle file
pickle_in = open("static/classifier.pkl", "rb")
classifier = pickle.load(pickle_in)


def predictnote(request):
    if request.method == 'POST':
        print("good")
        variance = request.POST['variance']
        skewness = request.POST['skewness']
        curtosis = request.POST['curtosis']
        entropy = request.POST['entropy']
        prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
        if prediction == 1:
            predict = "Authentic"
            context = {"msg1": "predicted value for  " + str([variance, skewness, curtosis, entropy]) + "  is  " + str(
                predict)}
        else:
            predict = "Not Authentic"
            context = {"msg2": "predicted value for  " + str([variance, skewness, curtosis, entropy]) + "  is  " + str(
                predict)}
        return render(request, "predict.html", context)
    return render(request, "predict.html", {"msg": "something went wrong!"})


def predict_file(request):
    if request.method == "POST":
        file = request.FILES['file']
        data = pd.read_csv(file)
        prediction = classifier.predict(data)
        context = {"msg1": "predicted value are " + str(prediction)}
        return render(request, "predict_file.html", context)
    return render(request, "predict_file.html", {"msg": "something went wrong!"})