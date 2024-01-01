from django.contrib import admin
from .models import *
# Register your models here.
class registerAdmin(admin.ModelAdmin):
    list_display=('name','email','mobile','ppic','passwd','address','cpasswd')
admin.site.register(register,registerAdmin)
######################################################################################
class categoryAdmin(admin.ModelAdmin):
    list_display=('id','Name')
admin.site.register(category,categoryAdmin)

##########################################################################################

class workerAdmin(admin.ModelAdmin):
    list_display=('id','name','email','aadhar','pan','phone','aphone','job','date','city')
admin.site.register(worker,workerAdmin)    