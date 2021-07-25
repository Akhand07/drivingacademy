from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse
from .models import Trainee, CustomUser, SchoolDetails, Tips, Feedback
from django.utils import timezone




def home(request):
    schooldata = SchoolDetails.objects.all()
    viewdata = Tips.objects.all()
    feedbackdata = Feedback.objects.all()
    schooldict = {
        "schooldetails": schooldata, "viewtips": viewdata, "feedbackdetails": feedbackdata
    }
    return render(request, 'index.html', schooldict)


def schooladmin(request):
    return render(request, 'schooladmin/schooladmin.html')


def maintemp(request):
    return render(request, 'schooladmin/maintemp.html')


def trainerhomepage(request):
    return render(request, 'trainer_task/trainerhomepage.html')


def traineetemp(request):
    return render(request, 'trainee/traineetemp.html')


def onlinetraineeadmission(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        firstname = request.POST["fname"]
        lastname = request.POST["lname"]
        city = request.POST["city"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        gender = request.POST["gender"]
        mode = request.POST["mode"]
        if mode == "online":
            status = "notconfirm"
        else:
            status = "confirm"
        fee = request.POST.get("fees")
        tdetails = request.POST.get("tdetails")

        if len(password) < 8:
            messages.error(request, "Password must be >8")
            # return redirect("registration")
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
                      Status=status, first_name=firstname, last_name=lastname)
        trainee.save()
        messages.success(request, "Trainee Admission Done  Successfully")
    return redirect('/')

def handlelogin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        traineeid = request.POST.get('traineeid', False)
        password = request.POST.get('password', '000')

        print(username, pass1)
        myuser = authenticate(username=username, password=pass1) or authenticate(username=traineeid, password=password)
        if myuser is not None:
            request.session["userinfo"] = username
            login(request, myuser)

            if myuser.is_SchoolAdmin == True:
                return render(request, 'schooladmin/schooladmin.html')

            elif myuser.is_Trainer == True:
                return render(request, 'trainer_task/trainerhomepage.html')

            elif myuser.is_Trainee == True:
                name = request.session["userinfo"]
                traneedetails = CustomUser.objects.get(username=name)
                traineeid = traneedetails.id
                print(traineeid)
                if Trainee.objects.filter(trainee_id=traineeid,Status="confirm"):
                    return render(request, 'trainee/traineehomepage.html')
                else:
                    return render(request,'index.html')
        else:
            messages.warning(request, "Invalid credential, Please Signup First")
            return redirect('School Admin Login')

    return render(request, 'index.html')


def handlelogout(request):
    if 'userinfo' in request.session:
        del (request.session['userinfo'])
    logout(request)
    return redirect("/")


def admintemp(request):
    return render(request, 'schooladmin/admintemp.html')

