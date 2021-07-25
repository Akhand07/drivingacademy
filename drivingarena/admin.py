from django.contrib import admin
from .models import CustomUser,SchoolAdmin, Trainer,Trainee, SchoolDetails,ridedetail,Tips,ContactUs
from .forms import  CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
#Register your models here.

class CustomUserAdmin(UserAdmin):
    model=CustomUser
    add_form=CustomUserCreationForm
    fieldsets =(
        *UserAdmin.fieldsets,
        (
            'User Role',
            {
                'fields':
                    (
                        'is_SchoolAdmin',
                        'is_Trainer',
                        'is_Trainee',



                    )
            }
        )
    )
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(SchoolAdmin)
admin.site.register(Trainer)
admin.site.register(Trainee)
admin.site.register(ContactUs)
