from django.db import models

class Symptom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Disease(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    precaution = models.TextField()
    medications = models.TextField()
    workouts = models.TextField()
    diets = models.TextField()

    def __str__(self):
        return self.name

class SymptomDiseaseRelation(models.Model):
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    weight = models.FloatField(default=1.0)

    class Meta:
        unique_together = ('symptom', 'disease')