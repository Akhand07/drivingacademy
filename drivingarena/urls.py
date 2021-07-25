from django.contrib import admin
from django.urls import path
from . import views,schooladminviews, trainerviews, traineeviews



urlpatterns = [
    path("", views.home, name="home"),
    # path("home", views.home, name="home"),

    #.................. SCHOOL ADMIN TASK AND ALL..........................

    path('validate_username/', schooladminviews.validate_username,name="validate_username"),
    path('schooladmin/', views.schooladmin,name="schooladmin"),
    path('addtrainer/', schooladminviews.addtrainer,name="Add Trainer"),
    path('addtrainee/', schooladminviews.addtrainee,name="ADD TRAINEE SIGNUP"),
    path('school_details/', schooladminviews.school_details, name="school_details"),
    path('view_school_admin_profile/', schooladminviews.view_school_admin_profile, name="SHOW ADMIN DETAILS"),
    path('viewschooldetails/', schooladminviews.viewschooldetails, name="SHOW SCHOOL DETAILS"),
    path('viewtrainerprofile/', schooladminviews.viewtrainerprofile, name="SHOW TRAINER DETAILS"),
    path('view_trainee_profile/', schooladminviews.view_trainee_profile, name="SHOW TRAINEE DETAILS"),
    path('view_request/', schooladminviews.view_request, name="VIEW REQUEST"),
    #path('view_school_admin_profile/', views.view_school_admin_profile, name="SHOW ADMIN DETAILS"),
    path("asigntrainer/", schooladminviews.asigntrainer, name="asigntrainer"),
    path("confirmadmission/", schooladminviews.confirmadmission, name="confirmadmission"),
    path("deletetrainees/",schooladminviews.deletetrainees,name="deletetrainees"),
    # path("showtrainee_details/<int:trainee_id>/",schooladminviews.showtrainee_details,name="showtrainee_details"),
    path("trainee", schooladminviews.deletetrainees, name="deletetrainees"),
    path("view_feedback/", schooladminviews.view_feedback, name="view_feedback"),
    path("view_contactus/", schooladminviews.view_contactus, name="view_contactus"),
    path("trainer_wise_trainee/", schooladminviews.trainer_wise_trainee, name="Trainer wise trianee"),

    path('login/', views.handlelogin,name="School Admin Login"),
    path('logout/', views.handlelogout,name="School Admin Logout"),

    #...........ONLINE ADMISSION SIGUNP PAGE..............

    path('onlinetraineeadmission/', views.onlinetraineeadmission,name="ONLINE Trainee Signup"),


   #.............DASHBOARDS.................

    #path('dashboard/', views.dash, name="dashboard"),
    path('admintemp/', views.admintemp, name="Admin temp html"),
    path('maintemp/', views.maintemp, name="maintemp"),
    path('traineetemp/', views.traineetemp, name="traineetemp"),

    #...............TRAINER TASK...............

    path('trainerhomepage/', views.trainerhomepage, name="trainerhomepage"),
    path('view_inside_trainer_profile/', trainerviews.view_inside_trainer_profile, name="TRAINER DETAILS"),
    path('add_tips/', trainerviews.add_tips, name="ADD TIPS"),
    path('view_tips/', trainerviews.view_tips, name="VIEW TIPS"),
    path('ride_details/', trainerviews.ride_details, name="ride_details"),
    path('view_ride_details/', trainerviews.view_ride_details, name="RIDE DETAILS"),
    path('trainerwisetrainee/', trainerviews.trainerwisetrainee, name="ASSIGNED TRAINEES DETAILS"),

    #....trainee_home.....
    path('traineehome/', traineeviews.traineehome, name="traineehome"),
    path('view_insider_trainee_profile/', traineeviews.view_insider_trainee_profile, name="TRAINEE DETAILS"),
    path('feedback/', traineeviews.feedback, name="feedback"),
    path('view_ride/', traineeviews.view_ride, name="view_ride"),
    path('view_trainer/', traineeviews.view_trainer, name="view_trainer"),

]
