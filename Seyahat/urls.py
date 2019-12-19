from django.contrib import admin
from django.urls import path
from . import views

app_name = "seyahat"

urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addseyahat/',views.addseyahat,name="addseyahat"),
    path('seyahat/<int:id>',views.detail,name="detail"),
    path('update/<int:id>',views.updateSeyahat,name="update"),
    path('delete/<int:id>',views.deleteSeyahat,name="delete"),
    path('',views.seyahat,name="seyahat"),
    path('comment/<int:id>',views.addComment,name="comment"),
    
]