from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from algorithm import X_test, Y_pred
# from knn import X_test, Y_pred
from .models import Doctor
import joblib


# Create your views here.
def index(request):
    return render(request, "index.html")


#Starter
def starter(request):
    return render(request, "starter.html")


#Register
def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully! Please Log In')
            return redirect('index')

    else:
        f = UserCreationForm()

    return render(request, 'registration/register.html', {'form': f})

@login_required
#Home
def home(request):
    return render(request, "home.html")

#Doctor
def DoctorList(request):
    all_lists = Doctor.objects.all().order_by('name')
    return render(request, 'doctor_list.html', {'posts': all_lists})


#Result
def result(request):
    cls = joblib.load('heart.sav')
    lis = []
    lis.append(request.GET['age'])
    lis.append(request.GET['sex'])
    lis.append(request.GET['cp'])
    lis.append(request.GET['trestbps'])
    lis.append(request.GET['chol'])
    lis.append(request.GET['fbs'])
    lis.append(request.GET['restecg'])
    lis.append(request.GET['thalach'])
    lis.append(request.GET['exang'])
    lis.append(request.GET['oldpeak'])
    lis.append(request.GET['slope'])
    lis.append(request.GET['ca'])
    lis.append(request.GET['thal'])
    
    # print(lis)
    
    ans = cls.predict([lis])
    return render(request, "result.html", {'ans':ans, 'lis':lis})

    
    





