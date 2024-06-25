from django.contrib import admin
from .models import Slot,Period,Classes,Student,Course,Teacher,Superadmin,Attendance,CountClass

class SlotAdmin(admin.ModelAdmin):
    list_display = ("name", "get_associated_periods_details")

    def get_associated_periods_details(self, obj):
        all_periods = obj.allPeriods.all()
        details = []
        for period in all_periods:
            details.append(f"{period.get_days_display()}: {period.start_time}-{period.end_time}")
        return "\t".join(details)

    get_associated_periods_details.short_description = "Associated Periods Details"

admin.site.register(Slot, SlotAdmin)


class PeriodAdmin(admin.ModelAdmin):
  list_display = ("name", "days","start_time","end_time",)
  
admin.site.register(Period, PeriodAdmin)

class ClassesAdmin(admin.ModelAdmin) :
    list_display = ("name","get_curCourses")
    def get_curCourses(self, obj):
        curCourses = obj.curCourses.all()
        details = []
        for courses in curCourses:
            details.append(f"{courses.name} ")
        return "\n".join(details)

    get_curCourses.short_description = "Courses"

admin.site.register(Classes,ClassesAdmin)

class SuperadminAdmin(admin.ModelAdmin) :
    list_display = ("name",)

admin.site.register(Superadmin,SuperadminAdmin)



class StudentAdmin(admin.ModelAdmin):
    list_display = ("name","class_instance","phone","dob","username")

admin.site.register(Student,StudentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ("name","Class","get_teachers","slot","curCode")

    def get_teachers(self, obj):
        teacher = obj.teacher.all()
        details = []
        for t in teacher:
            details.append(f"{t.name}")
        return ",".join(details)

    get_teachers.short_description = "Teachers"

admin.site.register(Course,CourseAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name","phone","get_curCourses","username")
    def get_curCourses(self, obj):
        curCourses = obj.curCourses.all()
        details = []
        for courses in curCourses:
            details.append(f"{courses.name} ")
        return "\n".join(details)

    get_curCourses.short_description = "Courses"

admin.site.register(Teacher,TeacherAdmin)

class AttendanceAdmin(admin.ModelAdmin) :
    list_display = ("student","course","Date","status","codeEntered","deviceId")
admin.site.register(Attendance,AttendanceAdmin)

class CountClassAdmin(admin.ModelAdmin):
    list_display = ("course","date")
admin.site.register(CountClass,CountClassAdmin)

# Register your models here.