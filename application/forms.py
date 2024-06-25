from django import forms
from .models import Student,Superadmin,Course,Teacher,Classes,Slot,Attendance

class stuLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
         model = Student  
         
         fields = ['username', 'password']

class TeacherLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
         model = Teacher  
         
         fields = ['username', 'password']

class adminLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
         model =  Superadmin 
         
         fields = ['username', 'password']

class CourseForm(forms.ModelForm):
    teachers = forms.ModelMultipleChoiceField(
        queryset=Teacher.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Teachers'
    )

    class Meta:
        model = Course
        exclude = ['teacher','curCode'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize queryset for the teachers field to display teacher names
        teacher_names = [(teacher.id, teacher.name) for teacher in Teacher.objects.all()]
        self.fields['teachers'].choices = teacher_names
        if 'curCode' in self.fields:
         self.fields['curCode'].queryset = Course.objects.none()
         self.fields['curCode'].widget = forms.HiddenInput()  

    def save(self, *args, **kwargs):
        
        try:
            # Saving the form to get the instance
            instance = super().save(*args, **kwargs)
            
            # After saving the course, add it to the curCourses of related teachers
            for teacher in self.cleaned_data['teachers']:
                teacher.curCourses.add(instance)
            
            # Save selected teachers to the 'teacher' field of the current object
            instance.teacher.set(self.cleaned_data['teachers'])

           
            
        except Exception as e:
            print(f"Error occurred while saving course: {e}")

class TeacherForm(forms.ModelForm):
    
    class Meta:
        model = Teacher
        exclude = ['curCourses']  # Exclude curCourses field from the form

    def clean_username(self):
        username = self.cleaned_data['username']
        # Check if a teacher with the same username already exists
        if Teacher.objects.filter(username=username).exists():
            raise forms.ValidationError("A teacher with this username already exists.")
        return username

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set curCourses initially to empty
        if 'curCourses' in self.fields:
         self.fields['curCourses'].queryset = Teacher.objects.none()
         self.fields['curCourses'].widget = forms.HiddenInput()  # Hide curCourses field in the form


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_username(self):
        username = self.cleaned_data['username']
        
        if Student.objects.filter(username=username).exists():
            raise forms.ValidationError("A teacher with this username already exists.")
        return username

class ClassesForm(forms.ModelForm):
    class Meta :
        model = Classes
        fields = ['name']

    def addAllSlots(self):
        
        slots = Slot.objects.all()
        for slot in slots:
            self.instance.available_slots.add(slot)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set availableSlots initially to all slots and hide the field
        if 'availableSlots' in self.fields:
            self.addAllSlots()
            self.fields['availableSlots'].queryset = Slot.objects.none()
            self.fields['availableSlots'].widget = forms.HiddenInput()


        
    