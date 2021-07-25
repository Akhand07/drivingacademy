from django.contrib import messages
from django.shortcuts import render
from .models import Trainer, ridedetail, Tips, Trainee, CustomUser
from django.utils import timezone


def view_inside_trainer_profile(request):
    username=request.session['userinfo']
    trainer_dts = CustomUser.objects.get(username=username)
    trainerid = trainer_dts.id
    print(trainerid)
    trainer_data = Trainer.objects.get(trainer_id_id=trainerid)
    print(trainer_data)
    trainerdict = {
        "data": trainer_data
    }
    return render(request, 'trainer_task/view_inside_trainer_profile.html', trainerdict)

def ride_details(request):
    trainer_username=request.session['userinfo']
    trainer_details = CustomUser.objects.get(username=trainer_username)
    trainerid = trainer_details.id
    print(trainerid)

    # username = request.session['userinfo']
    if request.method == "POST":
        from_to = request.POST.get("from_to")
        time = request.POST.get("time")
        traineeperformance = request.POST.get("traineeperformance")
        traineeid = request.POST.get("cmbtrainee")
        messages.success(request, "Ride details has been saved successfully")

        # for id in traineeidlist:
        #     print(id)
        #     Trainee.objects.filter(trainee=id)

        messages.success(request, "Trainer Assigned Successfully")
        ride = ridedetail(from_to=from_to, timeduration=time, traineeperformance=traineeperformance, trainee=traineeid, getdate=timezone.now())
        ride.save()
    trainee_detail = Trainee.objects.filter(trainer_id=trainerid)
    return render(request, 'trainer_task/ride_details.html',context={"trainee":trainee_detail})

def view_ride_details(request):
    ridedata = ridedetail.objects.all()
    print(ridedetail)
    ridedict = {
        "ridedetails": ridedata
    }
    return render(request, 'trainer_task/view_ride_details.html', ridedict)

def add_tips(request):
    if request.method == "POST":
        tips_id = request.POST.get('tips_id')
        tipstext = request.POST.get('tipstext')
        username = request.POST.get('username')
        postdate = request.POST.get('postdate')

        tip = Tips(tipsid=tips_id, tipstext=tipstext, username=username, postdate=postdate)
        tip.save()
        return render(request, 'trainer_task/add_tips.html')
    return render(request, 'trainer_task/add_tips.html')


def view_tips(request):
    viewdata = Tips.objects.all()
    print(Tips)
    viewdict = {
        "viewtips": viewdata
    }
    return render(request, 'trainer_task/view_tips.html', viewdict)

def trainerwisetrainee(request):
    trainer_username=request.session['userinfo']
    trainer_details=CustomUser.objects.get(username=trainer_username)
    trainerid=trainer_details.id
    print(trainerid)
    trainee_detail=Trainee.objects.filter(trainer_id=trainerid)
    print(trainee_detail)
    user_trainees = CustomUser.objects.filter(id__in=trainee_detail)
    # for u in user_trainees:
    #     print(u.first_name)
    # print(user_trainees)

    return render(request, 'trainer_task/trainerwisetrainee.html',context={"trainee":trainee_detail,"user_trainee":user_trainees})

