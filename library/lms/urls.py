from . import views
from django.urls import path

app_name='lms'

urlpatterns=[ 
    path('',views.home,name='home'),
    path('login/',views.my_view,name='studentlogin'),
    path('signup/',views.studentsignup_view,name='signup'),
    path('success/',views.success,name='success'),
    path('adminlogin/',views.admin_view,name='adminlogin'),
    path('success_admin/',views.success_admin,name='success_admin'),
    path('addbook/',views.add_books,name='addbook'),
    path('viewbook/',views.Home.as_view(),name='viewbook'),
    path('update/<int:pk>',views.Update.as_view(),name='update'),
    path('delete/<int:pk>',views.Delete.as_view(),name='delete'),
    path('issuebook/',views.issuebook_view,name='issuebook'),
    path('viewissuedbook/',views.viewissuedbook_view,name='viewissuedbook'),
    path('viewissuedbookbystudent/',views.viewissuedbookbystudent,name='viewissuedbookbystudent'),
    path('logout/',views.logout,name='logout'),
   
]