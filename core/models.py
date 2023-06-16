from django.db import models
from django.urls import reverse


class Record(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    email = models.EmailField()
    tel_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_absolute_url(self):
        return reverse('record_detail', args=[str(self.pk)])