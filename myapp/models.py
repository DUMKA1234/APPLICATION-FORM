from django.db import models

class Application(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resumes/')
    dob = models.DateField()


class JobExperience(models.Model):
    company = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

class CityChoices(models.TextChoices):
    NEW_YORK = "porharcourt", "porharcourt"
    BORI = "Bori", "Bori"
    LAGOS = "logos", "lagos"
    HOUSTON = "Houston", "Houston"

class BioData(models.Model):
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=255)
    city = models.CharField(max_length=255, choices=CityChoices.choices)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.place_of_birth}, {self.city}"


class Education(models.Model):
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

class Role(models.Model):
    role = models.CharField(max_length=255)
















# from django.db import models

# class EmploymentApplication(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=20)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

# class BioData(models.Model):
#     application = models.OneToOneField(EmploymentApplication, on_delete=models.CASCADE)
#     address = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     state = models.CharField(max_length=255)
#     date_of_birth = models.DateField(null=True, blank=True)  # Allow null values
#     zip_code = models.CharField(max_length=10)
#     def __str__(self):
#         return f"{self.application.first_name} {self.application.last_name} Bio-Data"

# class Education(models.Model):
#     application = models.ForeignKey(EmploymentApplication, on_delete=models.CASCADE)
#     institution = models.CharField(max_length=255)
#     degree = models.CharField(max_length=255)
#     start_date = models.DateField()
#     end_date = models.DateField(null=True, blank=True)  # Optional for ongoing education

#     def __str__(self):
#         return f"{self.application.first_name} {self.application.last_name} - {self.degree} at {self.institution}"

# class JobExperience(models.Model):
#     application = models.ForeignKey(EmploymentApplication, on_delete=models.CASCADE)
#     company = models.CharField(max_length=255)
#     job_title = models.CharField(max_length=255)
#     start_date = models.DateField()
#     end_date = models.DateField(null=True, blank=True)  # Optional for current job

#     def __str__(self):
#         return f"{self.application.first_name} {self.application.last_name} - {self.job_title} at {self.company}"

# class Role(models.Model):
#     application = models.OneToOneField(EmploymentApplication, on_delete=models.CASCADE)
#     role = models.CharField(max_length=255)

#     def __str__(self):
#         return f"{self.application.first_name} {self.application.last_name} Role: {self.role}"











# class test(models.Model):
#     id =models.IntegerField(primary_key=True)
#     firstname=models.CharField(max_length=50)
#     Lastname=models.CharField(max_length=50)
#     age =models.IntegerField()

# class test2(models.Model):
#     test=models.ForeignKey(test,on_delete=models.CASCADE)
#     id =models.IntegerField(primary_key=True)
#     firstname=models.CharField(max_length=50)
#     Lastname=models.CharField(max_length=50)
#     age =models.IntegerField()

# class test3(models.Model):
#     test=models.ManyToManyField(test2)
#     id =models.IntegerField(primary_key=True)
#     firstname=models.CharField(max_length=50)
#     Lastname=models.CharField(max_length=50)
#     age =models.IntegerField()

# class test4(models.Model):
#     test =models.OneToOneField(test,on_delete=models.CASCADE)



    
    
