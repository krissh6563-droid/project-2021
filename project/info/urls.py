from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('home',views.home, name='home'),
    path('upload_file',views.upload_file, name='upload_file'), 
    path('encrypt',views.encrypt, name='encrypt'),  
    path('view_file',views.view_file, name='view_file'), 
    path('download',views.download, name='download'),
    #path('decrypt',views.decrypt, name='decrypt'),    
]
#+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

