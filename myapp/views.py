
# from django.shortcuts import render, redirect, get_object_or_404
# from .form import ApplicationForm, JobExperienceForm, BioDataForm, EducationForm, RoleForm
# from .models import Application

# def application(request):
#     if request.method == 'POST':
#         form = ApplicationForm(request.POST)
#         if form.is_valid():
#             application = form.save()
#             request.session['application_id'] = application.id  # Store application ID in session
#             return redirect('jobexperience')
#     else:
#         form = ApplicationForm()
#     return render(request, 'application.html', {'form': form})

# def jobexperience(request):
#     application_id = request.session.get('application_id')
#     if not application_id:
#         return redirect('application')

#     application = get_object_or_404(Application, id=application_id)

#     if request.method == 'POST':
#         form = JobExperienceForm(request.POST)
#         if form.is_valid():
#             jobexperience = form.save(commit=False)
#             jobexperience.application = application
#             jobexperience.save()
#             return redirect('biodata')
#     else:
#         form = JobExperienceForm()
    
#     return render(request, 'jobexperience.html', {'form': form})

# def biodata(request):
#     application_id = request.session.get('application_id')
#     if not application_id:
#         return redirect('application')

#     application = get_object_or_404(Application, id=application_id)

#     if request.method == 'POST':
#         form = BioDataForm(request.POST)
#         if form.is_valid():
#             biodata = form.save(commit=False)
#             biodata.application = application
#             biodata.save()
#             return redirect('education')
#     else:
#         form = BioDataForm()

#     return render(request, 'biodata.html', {'form': form})

# def education(request):
#     application_id = request.session.get('application_id')
#     if not application_id:
#         return redirect('application')

#     application = get_object_or_404(Application, id=application_id)

#     if request.method == 'POST':
#         form = EducationForm(request.POST)
#         if form.is_valid():
#             education = form.save(commit=False)
#             education.application = application
#             education.save()
#             return redirect('role')
#     else:
#         form = EducationForm()

#     return render(request, 'education.html', {'form': form})

# def role(request):
#     application_id = request.session.get('application_id')
#     if not application_id:
#         return redirect('application')

#     application = get_object_or_404(Application, id=application_id)

#     if request.method == 'POST':
#         form = RoleForm(request.POST)
#         if form.is_valid():
#             role = form.save(commit=False)
#             role.application = application
#             role.save()
#             return redirect('success')
#     else:
#         form = RoleForm()

#     return render(request, 'role.html', {'form': form})

# def delete_job_experience(request, pk):
#     job_experience = JobExperience.objects.get(pk=pk)
#     job_experience.delete()
#     return redirect('job_experience')

# def edit_job_experience(request, pk):
#     job_experience = JobExperience.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = JobExperienceForm(request.POST, instance=job_experience)
#         if form.is_valid():
#             form.save()
#             return redirect('job_experience')
#     else:
#         form = JobExperienceForm(instance=job_experience)
#     return render(request, 'edit_job_experience.html', {'form': form})

# def delete_bio_data(request, pk):
#     bio_data = BioData.objects.get(pk=pk)
#     bio_data.delete()
#     return redirect('bio_data')

# def edit_bio_data(request, pk):
#     bio_data = BioData.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = BioDataForm(request.POST, instance=bio_data)
#         if form.is_valid():
#             form.save()
#             return redirect('bio_data')
#     else:
#         form = BioDataForm(instance=bio_data)
#     return render(request, 'edit_bio_data.html', {'form': form})

# def delete_education(request, pk):
#     education = Education.objects.get(pk=pk)
#     education.delete()
#     return redirect('education')

# def edit_education(request, pk):
#     education = Education.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = EducationForm(request.POST, instance=education)
#         if form.is_valid():
#             form.save()
#             return redirect('education')
#     else:
#         form = EducationForm(instance=education)
#     return render(request, 'edit_education.html', {'form': form})

# def edit_role(request, pk):
#     role = Role.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = RoleForm(request.POST, instance=role)
#         if form.is_valid():
#             form.save()
#             return redirect('role')
#     else:
#         form = RoleForm(instance=role)
#     return render(request, 'edit_role.html', {'form': form})


from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, redirect
from .form import ApplicationForm
from .form import BioDataForm
from .form import EducationForm
from .form import JobExperienceForm
from .form import RoleForm



def application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('biodata')
    else:
        form = ApplicationForm()
    return render(request, 'application.html', {'form': form})


def jobexperience(request):
    if request.method == 'POST':
        form = JobExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('role')
    else:
        form = JobExperienceForm()
    return render(request, 'jobexperience.html', {'form': form})

def biodata(request):
    if request.method == 'POST':
        form = BioDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('education')
    else:
        form = BioDataForm()
    return render(request, 'biodata.html', {'form':form})

def education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobexperience')
    else:
        form = EducationForm()
    return render(request, 'education.html', {'form':form})

def role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = RoleForm()
    return render(request, 'role.html', {'form':form})
def success(request):
    return render(request, 'success.html')






# # Create your views here.
# # def home(request):
# #     return HttpResponse('Hello World')

# # def contact(request):
# #     return HttpResponse('contact page')

# # def about_us(request):
# #     return HttpResponse('about_us page')


# # def product(request):
# #     return HttpResponse('product page')
# # def cart(request):
# #     return HttpResponse('cart page')
# # def order(request):
# #     return HttpResponse('order page')
# # def payment(request):
# #     return HttpResponse('payment page')
# # def registration(request):
# #     return HttpResponse('registration page')
# # def login(request):
# #     return HttpResponse('login page')