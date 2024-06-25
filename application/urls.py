from django.urls import path
from . import views
from django.views.generic.base import TemplateView 

urlpatterns = [
     path('',views.main,name = 'main'),
     path('studentLogin',views.studentLogin,name = 'StudentLogin'),
     path('adminLogin',views.adminLogin,name = 'Admin login'),
     path('teacherLogin',views.teacherLogin,name = 'teacher login'),
     path('Superadmin',views.admin,name = 'Superadmin'),
     path('Superadmin/newcourse',views.addCourse,name = 'NewCourse'),
     path('Superadmin/newTeacher',views.addTeacher,name = 'NewTeacher'),
     path('Superadmin/newStudent',views.addStudent,name = 'NewStudent'),
     path('Superadmin/newClass',views.addClass,name = 'NewClass'),
     path('Superadmin/allCourses',views.allCourses,name = 'AllCoursesList'),
     path('Superadmin/details/<int:id>',views.courseDetails,name = 'Details'),
     path('Superadmin/edit/<int:id>',views.courseEdit,name = 'Update'),
     path('Superadmin/delete/<int:id>',views.course_delete,name = 'Delete'),
     path('Teacher',views.teacher,name ='Teacher'),
     path('Teacher/myTimetable',views.teacherTimetable,name = 'Teacher Timetable'),
     path('Teacher/Codegeneration/<int:id>',views.Codegeneration,name = 'Codegeneration'),
     path('Student',views.student,name='Student'),
     path('Student/myTimetable',views.studentTimetable,name='Student Timetable'),
     path('Teacher/Close link/<int:id>',views.CloseLink,name = 'CloseLink'),
     path('Student/EnterCode/<int:id>',views.EnterCode,name = 'EnterCode'),
     path('Student/SubmitCode/<int:id>',views.SubmitCode,name = 'SubmitCode'),
     path('Teacher/MyCourses',views.teachercourses,name='Teacher Courses'),
     path('Teacher/MyCourses/<int:id>',views.coursewise,name = 'Details'),
     path('Student/My Attendance',views.stuAttendance,name = "My attendance"),
     path('logout',views.logout,name = 'logout'),

]