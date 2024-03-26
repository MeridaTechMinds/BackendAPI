from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("register",views.register),
    path("dashboard",views.applied_candidates,name="dashboard"),
    path("review_filter/<str:value>",views.review_filter),
    path("success",views.success),
    path("single_filter/<int:id>/",views.single_candidate),
    path("today_applied_list/",views.today_candidates),
    path("one_month_applied_list/",views.month_candidates),
    path("candidates_list/",views.total_candidates),
    path('download_selected/<str:value>', views.download_selected, name='download_selected'),
    path("messages",views.message_view,name="messages"),
    path("logout",views.user_logout),
    path('admin/hr_app/review/add/', views.add_review, name='add_review'),
    



  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)