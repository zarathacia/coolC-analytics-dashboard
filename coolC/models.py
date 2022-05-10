from django.db import models

# Create your models here.
class Measure(models.Model):
    Mvt = models.CharField(max_length=2)   
    Temp = models.IntegerField(default=0)
    Date = models.DateField()   
    Time = models.TimeField()
    TempExt= models.IntegerField(default=0)
    def __str__(self):
        txt=str(self.Mvt)+" "+str(self.Temp) +" "+ str(self.Date) +" " + str(self.Time) + " " + str(self.TempExt) 
        return txt