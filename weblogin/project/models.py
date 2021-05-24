from django.db import models
from django.contrib.auth.models import User  
# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE) 
    p_name= models.CharField(max_length=30)
    p_date=models.DateTimeField(auto_now=True)
    p_number= models.CharField(max_length=30)
    p_alt_number= models.CharField(max_length=30)
    p_locality=models.CharField(max_length=30)
    p_city=models.CharField(max_length=30)
    p_state=models.CharField(max_length=30)
    p_remark=models.CharField(max_length=30)

    #def serialize(self):
    '''    return{
            "id": self.id,
            "name":self.p_name,
            "Contact": self.p_number,
            "Alternate Contact": self.p_alt_number,
            "Locality": self.p_locality,
            "City": self.p_state,
            "State": self.p_state,
            "Remark": self.p_remark
        }'''
    def __str__(self):
        return f"{self.id} {self.p_name} {self.p_date} {self.p_number} {self.p_alt_number} {self.p_locality} {self.p_city} {self.p_state} {self.p_remark}"

class Oxygen(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE) 
    p_name= models.CharField(max_length=30)
    p_date=models.DateTimeField(auto_now=True)
    p_company=models.CharField(max_length=30)
    p_number= models.CharField(max_length=30)
    p_alt_number= models.CharField(max_length=30)
    p_locality=models.CharField(max_length=30)
    p_city=models.CharField(max_length=30)
    p_state=models.CharField(max_length=30)
    p_remark=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id} {self.p_name} {self.p_date} {self.p_company} {self.p_number} {self.p_alt_number} {self.p_locality} {self.p_city} {self.p_state} {self.p_remark}"


class Plasma(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE) 
    p_name= models.CharField(max_length=30)
    p_date=models.DateTimeField(auto_now=True)
    p_age=models.IntegerField()
    p_blood=models.CharField(max_length=30)
    p_number= models.CharField(max_length=30)
    p_alt_number= models.CharField(max_length=30)
    p_locality=models.CharField(max_length=30)
    p_city=models.CharField(max_length=30)
    p_state=models.CharField(max_length=30)
    p_remark=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id} {self.p_name} {self.p_date} {self.p_age} {self.p_blood} {self.p_number} {self.p_alt_number} {self.p_locality} {self.p_city} {self.p_state} {self.p_remark}"
   