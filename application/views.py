
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.shortcuts import get_object_or_404
from .forms import stuLoginForm,adminLoginForm,TeacherLoginForm,CourseForm,TeacherForm,StudentForm,ClassesForm
from .models import Student,Superadmin,Teacher,Course,Attendance,CountClass
from django.contrib import messages
from datetime import datetime
import random
from django.urls import reverse
import string
from django.utils import timezone




def main(request):
     request.session['flag'] = 0
     template = loader.get_template("main.html")
     context = {'flag': request.session['flag']}
     return HttpResponse(template.render(context,request))


def studentLogin(request):
    if request.method == "POST":
           form = stuLoginForm(request.POST)
           if form.is_valid() :
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            for student in Student.objects.all():
                if student.username == username and student.password == password:
                    request.session['id'] = student.id
                    request.session['flag'] = 1
                    return redirect("Student")
            else:
                # If no student found with given credentials, re-render the form with errors
                form.add_error(None, "Invalid username or password")
    else:
        form = stuLoginForm()

    context = {'form': form,
               'flag': request.session['flag']}
    return render(request, "studentLogin.html", context)

def teacherLogin(request):
    if request.method == "POST":
           form = TeacherLoginForm(request.POST)
           if form.is_valid() :
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            for teacher in Teacher.objects.all():
                if teacher.username == username and teacher.password == password:
                    request.session['id'] = teacher.id
                    request.session['flag'] = 1
                    return redirect("Teacher")
            else:
                # If no student found with given credentials, re-render the form with errors
                form.add_error(None, "Invalid username or password")
    else:
        form = TeacherLoginForm()

    context = {'form': form,
               'flag': request.session['flag']}
    return render(request, "TeacherLogin.html", context)

def adminLogin(request):
    if request.method == "POST":
           form = adminLoginForm(request.POST)
           if form.is_valid() :
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            for admin in Superadmin.objects.all():
                if admin.username == username and admin.password == password:
                    request.session['id'] = admin.id
                    request.session['flag'] = 1
                    return redirect("Superadmin")
            else:
                # If no student found with given credentials, re-render the form with errors
                form.add_error(None, "Invalid username or password")
    else:
        form = adminLoginForm()

    context = {'form': form,
               'flag': request.session['flag']}
    return render(request, "adminLogin.html", context)

def admin(request) :
  if request.session['flag'] == 1 :
    
    Sadmin = Superadmin.objects.get(id = request.session['id'])
    template = loader.get_template("Superadmin.html")
    context = {
        'Sadmin' : Sadmin,
        'flag': request.session['flag']
    }
   
    return HttpResponse(template.render(context,request))

def addCourse(request) :
    if request.session['flag'] == 1 :
       
        if request.method == "POST" :
            
            form = CourseForm(request.POST) 
            if form.is_valid() :
                form.save()
                x = form.cleaned_data['Class']
                courseName = form.cleaned_data['name']
                course = Course.objects.get(name = courseName)
                x.curCourses.add(course)
                if course.slot in x.availableSlots.all():
                    x.availableSlots.remove(course.slot)

            
                
                return redirect("Superadmin")
            
        else:
          form = CourseForm()  

        template = loader.get_template('AddCourse.html')
        context = {
    'form': form,
    'flag': request.session['flag']
  }
        return HttpResponse(template.render(context, request))
    else :
        messages.add_message(request, messages.WARNING, 'Please login to continue.')
        return redirect('Admin login')
    
def addTeacher(request):
    if request.session['flag'] == 1 :
       
        if request.method == "POST" :
            
            form = TeacherForm(request.POST) 
            if form.is_valid() :
                form.save()
                
                return redirect("Superadmin")
            
        else:
          form = TeacherForm()  

        template = loader.get_template('AddTeacher.html')
        context = {
    'form': form,
    'flag': request.session['flag']
  }
        return HttpResponse(template.render(context, request))
    else :
         messages.add_message(request, messages.WARNING, 'Please login to continue.')
         return redirect('Admin login')
    

def addStudent(request):
    if request.session['flag'] == 1 :
       
        if request.method == "POST" :
            
            form = StudentForm(request.POST) 
            if form.is_valid() :
                form.save()
                
                return redirect("Superadmin")
            
        else:
          form = StudentForm()  

        template = loader.get_template('AddStudent.html')
        context = {
    'form': form,
    'flag': request.session['flag']
  }
        return HttpResponse(template.render(context, request))
    else :
        messages.add_message(request, messages.WARNING, 'Please login to continue.')
        return redirect('Admin login')
    
def addClass(request):
    if request.session['flag'] == 1 :
       
        if request.method == "POST" :
            
            form = ClassesForm(request.POST) 
            if form.is_valid() :
                form.save()
                
                return redirect("Superadmin")
            
        else:
          form = ClassesForm()  

        template = loader.get_template('AddClasses.html')
        context = {
    'form': form,
    'flag': request.session['flag']
  }
        return HttpResponse(template.render(context, request))
    else :
        messages.add_message(request, messages.WARNING, 'Please login to continue.')
        return redirect('Admin login')

def allCourses(request) :

    if request.session['flag'] == 1 :
        allCourses = Course.objects.all().values()
        template = loader.get_template('AllCourses.html')
        context = {
            'allCourses' : allCourses,
            'flag' : request.session['flag'],
        }
        return HttpResponse(template.render(context,request))
    else :
        messages.add_message(request, messages.WARNING, 'Please login to continue.')
        return redirect('Admin login')
    
def courseDetails(request,id) :
 
 if request.session['flag'] == 1 :

  course = Course.objects.get(id=id)
  teachers = course.teacher.all()
  template = loader.get_template('Coursedetails.html')
  context = {
    'course': course,
    'teachers': teachers,
    'flag': request.session['flag']
  }
  return HttpResponse(template.render(context, request))
 else :
     messages.add_message(request, messages.WARNING, 'Please login to continue.')
     return redirect('Admin login')
 

def courseEdit(request, id):
  if request.session['flag'] == 1 :  
    course = Course.objects.get(id=id)
    
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect(f"/Superadmin/details/{course.id}")
    else:
        form = CourseForm(instance=course)
    
    template = loader.get_template('AddCourse.html')
    context = {
        'form': form,
        'flag': request.session['flag']
    }
    return HttpResponse(template.render(context, request))
  else :
    messages.add_message(request, messages.WARNING, 'Please login to continue.')
    return redirect('Admin login')


def course_delete(request, id):
   if request.session['flag'] == 1 : 
    course = get_object_or_404(Course, id=id)
    course_name = course.name  # Retrieve course name for the message
    course.delete()
    messages.success(request, f"Course '{course_name}' has been successfully deleted.")
    return redirect('/Superadmin/allCourses') 
   else :
     messages.add_message(request, messages.WARNING, 'Please login to continue.')
     return redirect('Admin login')

def teacher(request) :
 if request.session['flag'] == 1 :
    
    teacher = Teacher.objects.get(id = request.session['id'])
    template = loader .get_template('Teacher.html')
    context = {
        'teacher' : teacher,
        'flag': request.session['flag']
    }
   
    return HttpResponse(template.render(context,request))
 else :
     messages.add_message(request, messages.WARNING, 'Please login to continue.')
     return redirect('teacher login')
 
def teacherTimetable(request) :
  if request.session['flag'] == 1 :
     teacher = Teacher.objects.get(id = request.session['id'])
     curCourses = teacher.curCourses.all()
     now = datetime.now()
   
     current_day = now.strftime('%A')
     template = loader.get_template("teacherTimetable.html")
     context ={
        'teacher' : teacher,
         'curDay' : current_day,
         'curCourses' : curCourses,
         'flag': request.session['flag']
     }

     return HttpResponse(template.render(context,request))
     
  else :
     messages.add_message(request, messages.WARNING, 'Please login to continue.')
     return redirect('teacher login')




def student(request) :
 if request.session['flag'] == 1 :
    
    student = Student.objects.get(id = request.session['id'])
    template = loader .get_template('Student.html')
    context = {
        'student' : student,
        'flag': request.session['flag']
    }
   
    return HttpResponse(template.render(context,request))
 else :
     messages.add_message(request, messages.WARNING, 'Please login to continue.')
     return redirect('StudentLogin')
 
def studentTimetable(request) :
  if request.session['flag'] == 1 :
     student = Student.objects.get(id = request.session['id'])
     curCourses = student.class_instance.curCourses.all()
     now = datetime.now()
   
     current_day = now.strftime('%A')
     template = loader.get_template("studentTimetable.html")
     context ={
        'student' : student,
         'curDay' : current_day,
         'curCourses' : curCourses,
         'flag': request.session['flag']
     }

     return HttpResponse(template.render(context,request))
     
  else :
     messages.add_message(request, messages.WARNING, 'Please login to continue.')
     return redirect('StudentLogin')
  
     
      

    
def generate_random_code(length=6):
    # Define the characters you want to use for generating the code
    characters = string.ascii_letters + string.digits
    # Generate a random code of specified length
    random_code = ''.join(random.choice(characters) for _ in range(length))
    return random_code

def Codegeneration(request,id):
  if request.session['flag'] == 1 :
    if request.method == 'POST':
        course = Course.objects.get(id = id)
        template = loader.get_template("codeDisplay.html")
       
    # Generate a random code
        random_code = generate_random_code()
        
        course.curCode = random_code
        course.save()
        count_instance =CountClass.objects.create(
           course = course,
           date = timezone.now().date(),
        )
        context ={
            'code' : course.curCode,
            'course' : course,
            'flag': request.session['flag']
        }
        return HttpResponse(template.render(context,request))
  else :
    messages.add_message(request, messages.WARNING, 'Please login to continue.')
    return redirect('teacher login')
  
def CloseLink(request,id):
  if request.session['flag'] == 1 :
    
        course = Course.objects.get(id = id)
        course.curCode = 'None'
        course.save()
          
        return redirect('/Teacher/myTimetable')
  else :
    messages.add_message(request, messages.WARNING, 'Please login to continue.')
    return redirect('teacher login')
  
def EnterCode(request, id):
    if request.session.get('flag') == 1:
        # if request.method == "POST":
            template = loader.get_template('enterCode.html')
            course = Course.objects.get(id=id)
            context = {'id': id, 'course': course,
                       'flag': request.session['flag']}
            
            
           
            return HttpResponse(template.render(context,request))

    else:
        messages.add_message(request, messages.WARNING, 'Please login to continue.')
        return redirect('StudentLogin')
    
# Form saving
def SubmitCode(request,id) :
     if request.session['flag'] == 1 :
       if request.method == 'POST':
            
            entered_code = request.POST.get('code', '')
            course = Course.objects.get(id=id)
            student = Student.objects.get(id=request.session.get('id'))
            
            if entered_code == course.curCode and entered_code != 'None':
                status = 'P'
            else:
                status = 'A'

            attendance_instance = Attendance.objects.create(
                student=student,
                course=course,
                Date=timezone.now().date(),
                status=status,
                codeEntered=entered_code,
                deviceId = request.META.get('REMOTE_ADDR')

            )
            return redirect('/Student/myTimetable')
     else :
       messages.add_message(request, messages.WARNING, 'Please login to continue.')
       return redirect('StudentLogin')
     
def stuAttendance(request) :
  if request.session['flag'] == 1 :
    student = get_object_or_404(Student,id = request.session['id'])
    courses = student.class_instance.curCourses.all()
    date = timezone.now().date()
    if request.method == 'GET':
     template = loader.get_template('MyAttendance.html')
    
     
     
     context = {
        'courses' : courses,
         'date' : date,
         'flag': request.session['flag']
     }
     return HttpResponse(template.render(context,request))
    else :
            template = loader.get_template('MyAttendance.html')
          
            courses = student.class_instance.curCourses.all()
            start_date_str = request.POST.get('start_date')
            end_date_str = request.POST.get('end_date')
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()

            template = loader.get_template('MyAttendance.html')
            student = get_object_or_404(Student,id = request.session['id'])
            courses = student.class_instance.curCourses.all()
            totalCount = {}
            presentCount ={}

# Iterate over courses and corresponding counts
            for x in courses :
               cnt = 0
               cnt1 =0
               total_count = CountClass.objects.filter(course=x, date__range=(start_date, end_date)).count()
               totalCount[x.id] = total_count
               for i in Attendance.objects.all():
                 if i.course == x and i.student == student and i.status == 'P' :
                    cnt1 = cnt1+1
               presentCount[x.id] = cnt1
                 
                  
     
            context = {
        'courses' : courses,
         'date' : date,
         'totalcount' : totalCount,
         'presentCount' : presentCount,
         'flag': request.session['flag']
     }
            return HttpResponse(template.render(context,request))
     
  else :
    messages.add_message(request, messages.WARNING, 'Please login to continue.')
    return redirect('StudentLogin')

def teachercourses(request) :
  if request.session['flag'] == 1 :
     teacher = Teacher.objects.get(id = request.session['id'])
     curCourses = teacher.curCourses.all()
    
     template = loader.get_template("teachercourses.html")
     context ={
        'teacher' : teacher,
         
         'curCourses' : curCourses,
         'flag': request.session['flag']
     }

     return HttpResponse(template.render(context,request))
     
  else :
    messages.add_message(request, messages.WARNING, 'Please login to continue.')
    return redirect('teacher login')
  
def coursewise(request, id):
    if request.session.get('flag') == 1:
        course = get_object_or_404(Course, id=id)
        Class = course.Class
        stuList = Student.objects.filter(class_instance=Class)

        date = timezone.now().date()
        if request.method == 'GET':
            template = loader.get_template('Coursewise.html')
            context = {
                'stuList': stuList,
                'date': date,
                'course' : course,
                'flag': request.session['flag']
            }
            return HttpResponse(template.render(context, request))
        else:
            template = loader.get_template('Coursewise.html')
            start_date_str = request.POST.get('start_date')
            end_date_str = request.POST.get('end_date')
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()

            totalCount_list = {}
            presentCount_list = {}

            for student in stuList:
                
               

                
                total_count = CountClass.objects.filter(course=course, date__range=(start_date, end_date)).count()
               
                present_count = Attendance.objects.filter(course=course, student=student, status='P', Date__range=(start_date, end_date)).count()
               

                totalCount_list[student.id] = total_count
                presentCount_list[student.id] = present_count

            context = {
                'stuList': stuList,
                'date': date,
                'start_date': start_date,
                'end_date' : end_date,
                 'course' : course,
                'totalCount_list': totalCount_list,
                'presentCount_list': presentCount_list,
                'flag': request.session['flag']
            }
            return HttpResponse(template.render(context, request))
    else:
       messages.add_message(request, messages.WARNING, 'Please login to continue.')
       return redirect('teacher login')
    
def logout(request) :
   request.session['flag'] = 0
   return redirect('')



      
      















