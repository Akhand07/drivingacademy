from django.contrib import messages
# from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .models import Feedback, Trainee, Trainer, CustomUser, ridedetail
from django.utils import timezone
# from datetime import datetime


def traineehome(request):
    return render(request, 'trainee/traineehomepage.html')

def view_insider_trainee_profile(request):
    username=request.session['userinfo']
    trainee_dts = CustomUser.objects.get(username=username)
    traineeid = trainee_dts.id
    print(traineeid)
    trainee_data = Trainee.objects.get(trainee_id=traineeid)
    print(trainee_data)
    traineedict = {
        "data": trainee_data
    }
    return render(request, 'trainee/view_insider_trainee_profile.html', traineedict)



def feedback(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            username = request.session["userinfo"]
            rating = request.POST.get('rating')
            feedback = request.POST.get("feedback")

            feed = Feedback(username=username, feedback_text=feedback, rating=rating, date=timezone.now())
            feed.save()

            messages.success(request, "Thanks for giving your valuable feedback")
    return render(request, 'trainee/feedback.html')


def view_ride(request):
    username = request.session["userinfo"]
    data = CustomUser.objects.get(username=username)
    traineeid = data.id
    ridedata = ridedetail.objects.filter(trainee=traineeid)
    param= {
        "viewdata": ridedata

    }
    return render(request, 'trainee/view_ride.html', param)


def view_trainer(request):
    username = request.session["userinfo"]
    data = CustomUser.objects.get(username=username)
    traineeid = data.id
    Trainee.objects.get(trainee_id=traineeid)
    traineedetails = Trainee.objects.get(trainee_id=traineeid)
    trainerid = traineedetails.trainer_id
    if Trainer.objects.filter(trainer_id_id=trainerid):
        trainerdetails = Trainer.objects.get(trainer_id_id=trainerid)
        print(trainerdetails)
        usertrianer = CustomUser.objects.get(id=trainerid)
        param = {
            "view": trainerdetails,
            "details": usertrianer
        }
        return render(request, 'trainee/view_trainer.html', param)

    else:
        return render(request, 'trainee/view_trainer.html')
