from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Period(models.Model) :
    name = models.CharField(max_length = 3)
    DAYS_OF_WEEK = [
    ('0', 'Monday'),
    ('1', 'Tuesday'),
    ('2', 'Wednesday'),
    ('3', 'Thursday'),
    ('4', 'Friday'),
    
    ]

    days = models.CharField( max_length= 10,choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
     return f"{self.name}"

    
    
class Slot(models.Model):
   name = models.CharField(max_length = 2)

   allPeriods = models.ManyToManyField(Period)
   
   def __str__(self):
    return f"{self.name}"
   
   

class Classes(models.Model) :
  
  name = models.CharField(max_length=255)

  availableSlots = models.ManyToManyField('Slot', related_name='classes', blank=True)
  curCourses = models.ManyToManyField('Course', related_name='assigned_class', blank=True)


  def __str__(self):
    return f"{self.name}"

class Student(models.Model):
  name = models.CharField(max_length=255)
  class_instance = models.ForeignKey(Classes, on_delete=models.CASCADE,null = True)
  phone = models.IntegerField(null=True)
  dob = models.DateField(null=True)
  username = models.CharField(max_length = 255,default =" ")
  password = models.CharField(max_length = 15, blank=False, null=False,default='')

  def __str__(self):
    return f"{self.name} "
  
class Superadmin(models.Model):
  name = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  dob = models.DateField(null=True)
  username = models.CharField(max_length = 255,default =" ")
  password = models.CharField(max_length = 15, blank=False, null=False,default='')

  def __str__(self):
    return f"{self.name} "
  


class Course(models.Model):
    name = models.CharField(max_length=255)
    Class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    teacher = models.ManyToManyField('Teacher', related_name='courses', blank=True)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)  # Each course has one slot
    # activeLink = models.IntegerField(max_length =1, default = "0")
    curCode = models.CharField(max_length = 10,default = "None")

    def __str__(self):
       return f"{self.name}"
    
      

class Teacher(models.Model):
  name = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  dob = models.DateField(null=True)
  username = models.CharField(max_length = 255,default =" ")
  password = models.CharField(max_length = 15, blank=False, null=False,default='')
 
  curCourses = models.ManyToManyField(Course, related_name='assigned_teachers', blank=True)


  def add_course(self, course):
        self.curCourses.add(course)

  def remove_course(self, course):
        self.curCourses.remove(course)

  def __str__(self):
       return f"{self.name}"
    


class Attendance(models.Model):
   
   statusChoices = [
      ('P','Present'),
      ('A','Absent'),
   ]
   student = models.ForeignKey('Student',on_delete = models.DO_NOTHING,default = "")
   course = models.ForeignKey(Course,on_delete = models.DO_NOTHING)
   Date = models.DateTimeField()
   status = models.CharField(max_length = 10,choices = statusChoices )
  # teacher = models.ForeignKey('Teacher',on_delete = models.DO_NOTHING)
   codeEntered = models.CharField(max_length = 10)
   deviceId = models.CharField(max_length = 255,default = "")

class CountClass(models.Model):
   
   course = models.ForeignKey(Course,on_delete = models.DO_NOTHING)
   date = models.DateField()
