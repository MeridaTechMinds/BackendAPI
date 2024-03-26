from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from BlogApp.views import catagory_details,catagory,comments_list,contacts_data,apointment_data
urlpatterns = [
    path("data/<str:slug>",catagory_details ),
    path("datas/<str:Category>/",catagory ),
    path("comments",comments_list),
    path("contacts",contacts_data),
    path("apointments",apointment_data),
    path("subscription",views.subscription_data),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)