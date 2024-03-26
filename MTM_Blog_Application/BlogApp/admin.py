from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(contact)
admin.site.register(Apointment)
admin.site.register(Details)
admin.site.register(subscription)





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

class JobPortalAdmin(admin.ModelAdmin):
    autocomplete_fields = ['Requirements']  
    fieldsets = (
        (None, {
            'fields': ('Job_Title', 'Job_Location', 'Job_Type', 'No_of_Openings')
        }),
        ('Experience', {
            'fields': ('Min_Experience', 'Max_Experience'),
            'classes': ('wide',), 
        }),
       (None, {
            'fields': ('Requirements', 'Job_Discription')
        }),
    )
    

admin.site.register(Job_Portal, JobPortalAdmin)


class JobPointsModelAdmin(admin.ModelAdmin):
    search_fields = ['point']
admin.site.register(job_points, JobPointsModelAdmin)