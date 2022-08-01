from operator import index
from django.urls import path
from . import views


urlpatterns = [

    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'), 
    path('profile/',views.profile,name='profile'),  
    path('change-password/',views.change_password,name='change-password'),  
    path('edit-profile/',views.edit_profile,name='edit-profile'),
    path('addmember/',views.add_member,name='addmember'),
    path('addnotice/',views.add_notice,name='addnotice'),
    path('allnotice/',views.all_notice,name='allnotice'),
    path('addevents/',views.add_events,name='addevents'),
    path('allevents/',views.all_events,name='allevents'),
    path('member/',views.member,name='member'),

]
