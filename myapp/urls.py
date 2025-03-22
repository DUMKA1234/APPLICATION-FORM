
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('application/', views.application, name='application'),
#     path('jobexperience/', views.jobexperience, name='jobexperience'),
#     path('biodata/', views.biodata, name='biodata'),
#     path('education/', views.education, name='education'),
#     path('role/', views.role, name='role'),
    
#     path('delete-job_experience/<int:pk>/', views.delete_jobexperience, name='delete_job_bexperience'),
#     path('edit-job_experience/<int:pk>/', views.edit_jobexperience, name='edit_job_experience'),
#     path('delete-biodata/<int:pk>/', views.delete_biodata, name='delete_biodata'),
#     path('edit-biodata/<int:pk>/', views.edit_biodata, name='edit_biodata'),
#     path('delete-education/<int:pk>/', views.delete_education, name='delete_education'),
#     path('edit-education/<int:pk>/', views.edit_education, name='edit_education'),
#     path('delete-role/<int:pk>/', views.delete_role, name='delete_role'),
#     path('edit-role/<int:pk>/', views.edit_role, name='edit_role'),
# ]


from django.urls import path
from django.urls import path
from . import views
urlpatterns=[
    path('application/', views.application, name='application'),
    path('biodata/', views.biodata, name='biodata'),
    path('education/', views.education, name='education'),
    path('jobexperience/', views.jobexperience, name='jobexperience'),
    path('role/', views.role, name='role'),
    path('success/', views.success, name='success'), 
    
    

]
    


