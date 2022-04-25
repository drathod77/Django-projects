from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# from unixdatetimefield import UnixDateTimeField

# Create your models here.

class University(models.Model):

    university_name = models.CharField(max_length=255, unique=True)
    university_city = models.CharField(max_length=255)
    created_at = models.IntegerField()
    updated_at = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    updated_by = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='upadate_by' )

    def __str__(self):
        return self.university_name

    
class UniversityContacts(models.Model):
    contact_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15, validators=[RegexValidator(
        '^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$', message="Enter a Valid Indian Phone Number")])
    contact_type = models.CharField(max_length=255)
    contact_email = models.EmailField(unique=True)
    university_id = models.ForeignKey(University, on_delete = models.CASCADE)
    created_at = models.IntegerField()
    updated_at = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)
    updated_by = models.ForeignKey(User, on_delete = models.CASCADE,related_name='upadatedby')


    def __str__(self):
        return self.contact_name



    