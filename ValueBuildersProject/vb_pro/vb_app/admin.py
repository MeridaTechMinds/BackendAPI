from django.contrib import admin
from .models import *

class ImageModelAdmin(admin.ModelAdmin):
    search_fields = ['image',]
admin.site.register(image_model, ImageModelAdmin)
 
class PropertyModelAdmin(admin.ModelAdmin):
    autocomplete_fields = ['images'] 
    # class Media:
    #     js = ('js/district_script.js',) 
admin.site.register(PropertyModel,PropertyModelAdmin)

admin.site.register(contact)





