from django.db import models

# Create your models here.
class Mode(models.Model):
    nomi=models.CharField(max_length=500)
    izoh=models.CharField(max_length=200,blank=True, null=True)
    def __str__(self) -> str:
        return self.nomi
