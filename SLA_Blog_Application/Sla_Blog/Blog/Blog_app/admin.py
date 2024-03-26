from django.contrib import admin

# Register your models here.

from .models import *


# admin.site.register(contact)
# admin.site.register(Apointment)
# admin.site.register(Details)
admin.site.register(Enquiry_model)
admin.site.register(Instructor_model)
admin.site.register(Get_in_Touch)
admin.site.register(contact_details)


class propertyAdmin(admin.ModelAdmin):
    #filter_horizontal = ('images',)
    autocomplete_fields = ['points',"comments"]  
admin.site.register(Blog,propertyAdmin)


class PointModelAdmin(admin.ModelAdmin):
    search_fields = ['point']
admin.site.register(Points, PointModelAdmin)

class CommentModelAdmin(admin.ModelAdmin):
    search_fields = ['comments']
admin.site.register(Comments, CommentModelAdmin)

# class JobDiscriptionModelAdmin(admin.ModelAdmin):
#     autocomplete_fields = ['points']  
# admin.site.register(Job_Portal,JobDiscriptionModelAdmin)

# class JobPointsModelAdmin(admin.ModelAdmin):
#     search_fields = ['point']
# admin.site.register(job_points, JobPointsModelAdmin)