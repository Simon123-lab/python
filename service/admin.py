from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import *

# Register your models here.
admin.site.register(User)

class OrderAdminSite(admin.ModelAdmin):
    model = Order
    list_display = ('order_id','client','category','quantity','id_name','phone_no','amount','status')
    
admin.site.register(Order,OrderAdminSite)

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    modal = AssignOrder
    list_display = ('assign_id','link')
    pass

admin.site.register(AssignOrder, MyModelAdmin)
admin.site.register(Review)
admin.site.register(ContestEntries)
admin.site.register(FrequentlyAskQuestions)
admin.site.register(UpdateWeeklyContest)
admin.site.register(RobotConfirmationViews)


    