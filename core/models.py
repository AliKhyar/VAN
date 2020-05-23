from django.db import models

# Create your models here.

class Project(models.Model):
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    capitale = models.IntegerField()
    duration = models.DurationField()
    #Duree_end = models.DateField()
    year_cash_flow = models.IntegerField()
    taux_actualisation = models.FloatField(max_length=1)

    def __str__(self):
        return self.nom
    
    
