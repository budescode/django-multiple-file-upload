from django.db import models

class FileUpload(models.Model):
    name = models.CharField(max_length=20) 
    file = models.FileField() 
    def __str__(self):
        return self.name