from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .forms import ContactusForm
from .models import CustomUser, Trainer, Trainee, SchoolDetails, Feedback, SchoolAdmin, ContactUs
from django.utils import timezone
from datetime import datetime
from django.http import JsonResponse


def view_school_admin_profile(request):
    admindata = SchoolAdmin.objects.all()
    adminidentity = CustomUser.objects.filter(id__in=admindata)
    print(admindata)
    return render(request, 'schooladmin/view_school_admin_profile.html',context={"admindetails":admindata,"adminidentitydetails":adminidentity})

def addtrainer(request):
    if request.method == "POST" and request.FILES['fileupload']:
        # trainer_id = request.POST.get("trainer_id")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        firstname = request.POST.get("fname")
        lastname = request.POST.get("lname")
        experience = request.POST.get("experience")
        phone = request.POST.get("phone")
        city = request.POST.get("city")
        gender = request.POST.get("gender")
        address = request.POST.get("address")
        myfile = request.FILES['fileupload']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        imgdict = {
            'file_url': uploaded_file_url
        }

        if len(password) < 8:
            messages.error(request, "Password must be >8")
            return redirect("addtrainer")
        if not username.isalnum():
            messages.error(request, "Trainer accountname must be alpha numberic")
            return redirect("addtrainer")
        user = CustomUser.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = lastname
        user.is_Trainer = True

        user.save()
        trainer = Trainer(user.pk, dateofjoin=timezone.now(), photo=myfile.name, gender=gender,
                          phone=phone, address=address, experience=experience, city=city)
        trainer.save()
        messages.success(request, "Account has been Created  Successfully")
        return render(request, 'schooladmin/addtrainer.html', imgdict)

    return render(request, 'schooladmin/addtrainer.html', )

def viewtrainerprofile(request):
    trainerdata = Trainer.objects.all()
    print(Trainer)
    # trainerdict = {
    #     "trainerdetails": trainerdata
    # }
    trainer_name = CustomUser.objects.filter(is_Trainer=True)

    return render(request, 'schooladmin/viewtrainerprofile.html', context={"trainerdetails":trainerdata,"trainer_name_details":trainer_name})


def addtrainee(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        firstname = request.POST.get("fname")
        lastname = request.POST.get("lname")
        city = request.POST.get("city")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        mode = request.POST.get("mode")
        if mode == "online":
            status = "notconfirm"
        else:
            status = "confirm"
        fee = request.POST.get("fees")
        tdetails = request.POST.get("tdetails")

        if len(password) < 8:
            messages.error(request, "Password must be >8")
            return redirect("registration")
        if not username.isalnum():
            messages.error(request, "Trainer accountname must be alpha numberic")
            return redirect("addtrainer")
        myuser = CustomUser.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.is_Trainee = True

        myuser.save()
        date_string = "2021-06-30"
        adminssion_date = datetime.fromisoformat(date_string)
        trainee = Trainee(myuser.pk, City=city, Address=address, Phone=phone, Gender=gender,
                          DateOfAdmission=adminssion_date, Admissionmode=mode, Transactionnumber=tdetails, Fees=fee,
                          Status=status,first_name=firstname,last_name=lastname)
        trainee.save()
        messages.success(request, "Trainee Admission Done  Successfully")

    return render(request, 'schooladmin/addtrainee.html')

def view_trainee_profile(request):
    traineedata = Trainee.objects.all()
    print(Trainee)
    traineedict = {
        "traineedetails": traineedata
    }
    return render(request, 'schooladmin/view_trainee_profile.html', traineedict)

def school_details(request):
    if request.method == "POST":
        schoolName = request.POST.get("SchoolName")
        ownerName = request.POST.get("OwnerName")
        email = request.POST.get("email")
        address = request.POST.get("address")
        city = request.POST.get("city")
        phone = request.POST.get("phone")
        openingdays = request.POST.get("openingdays")
        timings = request.POST.get("timings")
        about = request.POST.get("about")

        compdetails = SchoolDetails(school_name=schoolName, owner_name=ownerName, city=city, address=address,
                                    phone=phone, email=email, about=about, opening_days=openingdays,
                                    time=timings)
        compdetails.save()
        messages.success(request, "School details has been saved successfully")
        return render(request, 'schooladmin/school_details.html')

    return render(request, 'schooladmin/school_details.html')

def viewschooldetails(request):
    schooldata = SchoolDetails.objects.all()
    print(SchoolDetails)
    schooldict = {
        "schooldetails": schooldata
    }
    return render(request, 'schooladmin/viewschooldetails.html', schooldict)

def view_request(request):
    view = Trainee.objects.all()
    print(view)
    viewdict = {
        "view_trainee_request": view
    }
    return render(request, 'schooladmin/view_request.html', viewdict)

def confirmadmission(request):
    if request.method == "POST":
        traineeidlist = request.POST.getlist("chk")
        for id in traineeidlist:
            print(id)
            Trainee.objects.filter(trainee_id=id).update(Status='confirm')
        messages.success(request, "Trainee Admission confirm  Successfully")

        print("Status updated")

    trainees = Trainee.objects.filter(Status='notconfirm')

    traineedict = {"trainees": trainees}

    return render(request, 'schooladmin/confirmadmission.html', traineedict)


def asigntrainer(request):
    if request.method == "POST":
        trainer_id = request.POST.get("cmbtrainer")
        traineeidlist = request.POST.getlist("chk")
        for id in traineeidlist:
            print(id)
            Trainee.objects.filter(trainee_id=id).update(trainer_id=trainer_id)
        messages.success(request, "Trainer Assigned Successfully")

    trainer = CustomUser.objects.filter(is_Trainer=True)
    trainees = Trainee.objects.filter(Status='confirm', trainer_id=None)
    user_trainees = CustomUser.objects.filter(id__in=trainees)

    return render(request, 'schooladmin/asigntrainer.html',
                  context={"trainer": trainer, "trainee": trainees, "user_trainees": user_trainees})

def deletetrainees(request):
    if request.method == "POST":
        traineeidlist = request.POST.getlist("chk")  # value from checkbox
        print(traineeidlist)
        for id in traineeidlist:
            print(id)
            CustomUser.objects.get(id=id).delete()

    user_trainee = CustomUser.objects.filter(is_Trainee=True)
    print(user_trainee)
    trainee_detail = {"user_trainee": user_trainee}
    return render(request, 'schooladmin/view_trainees_after_deletion.html', trainee_detail)



def view_feedback(request):
    feedbackdata = Feedback.objects.all()
    print(Trainer)
    feeddict = {
        "feedbackdetails": feedbackdata
    }
    return render(request, 'schooladmin/view_feedback.html', feeddict)


def view_contactus(request):
    contactusdata = ContactUs.objects.all()
    print(contactusdata)
    feeddict = {
        "contactdetails": contactusdata
    }
    return render(request, 'schooladmin/view_contactus.html', feeddict)

def validate_username(request):
    username = request.GET.get('username',None)
    print(username)
    data = {
        'is_taken': CustomUser.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

def trainer_wise_trainee(request):
    alltrainers= CustomUser.objects.filter(is_Trainer=True)
    return  render(request,'schooladmin/trainer_wise_trainee.html',alltrainers)

def ajax_trainee_details(request):
    trainerid=request.GET.get("tid")
    alltrainees=Trainee.objects.filter(trainer_id=trainerid)
    traineelist=alltrainees.values()
    mytraineelist=list(traineelist)

    return JsonResponse({"trainees": mytraineelist})