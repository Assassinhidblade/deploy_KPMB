from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),

    #course
    path('course/',views.course,name="course"),
    path('course/new_course',views.new_course,name='new_course'),
    path('search_course',views.search_course,name='search_course'),
    path('course/update_course/<str:code>',views.update_course,name='update_course'),
    path('course/update_course/save_update_course/<str:code>',views.save_update_course,name='save_update_course'),
    path('course/delete_course/<str:code>',views.delete_course,name='delete_course'),

    #student
    path('student/',views.student,name="student"),
    path('student/new_student',views.new_student,name='new_student'),

]