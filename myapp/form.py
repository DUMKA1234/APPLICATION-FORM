from django import forms
from .models import Application, JobExperience, BioData, Education, Role

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'address','resume')

class JobExperienceForm(forms.ModelForm):
    class Meta:
        model = JobExperience
        fields = ('company', 'job_title', 'start_date', 'end_date')

class BioDataForm(forms.ModelForm):
    class Meta:
        model = BioData
        fields = ('date_of_birth', 'place_of_birth', 'city','address')

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('institution', 'degree', 'start_date', 'end_date')

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ('role',)















# from django import forms
# from .models import EmploymentApplication, BioData, Education, JobExperience, Role

# class EmploymentApplicationForm(forms.ModelForm):
#     class Meta:
#         model = EmploymentApplication
#         fields = ('first_name', 'last_name', 'email', 'phone_number')

# class BioDataForm(forms.ModelForm):
#     class Meta:
#         model = BioData
#         fields = ('address', 'city', 'date_of_birth','state', 'zip_code')

# class EducationForm(forms.ModelForm):
#     class Meta:
#         model = Education
#         fields = ('institution', 'degree', 'start_date', 'end_date')

# class JobExperienceForm(forms.ModelForm):
#     class Meta:
#         model = JobExperience
#         fields = ('company', 'job_title', 'start_date', 'end_date')

# class RoleForm(forms.ModelForm):
#     class Meta:
#         model = Role
#         fields = ('role',)