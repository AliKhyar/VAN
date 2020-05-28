from django.db import models

# Create your models here.

class Project(models.Model):
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    capitale = models.FloatField()
    duration = models.DurationField()
    #Duree_end = models.DateField()
    year_cash_flow = models.CharField(max_length=200)
    taux_actualisation = models.FloatField()

    def __str__(self):
        return self.nom
    
    
