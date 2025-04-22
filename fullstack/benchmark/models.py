from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BenchmarkResult(models.Model):
    CPU_CHOICES = [
        ('i3', 'Intel Core i3'),
        ('i5', 'Intel Core i5'),
        ('i7', 'Intel Core i7'),
        ('r5', 'Ryzen 5'),
        ('r7', 'Ryzen 7'),
    ]
    GPU_CHOICES = [
        ('gtx1050', 'GTX 1050'),
        ('gtx1660', 'GTX 1660'),
        ('rtx3060', 'RTX 3060'),
        ('integrated', 'Integrated'),
    ]
    RAM_CHOICES = [
        ('8', '8 GB'),
        ('16', '16 GB'),
        ('32', '32 GB'),
    ]
    STORAGE_CHOICES = [
        ('hdd', 'HDD'),
        ('ssd', 'SSD'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cpu = models.CharField(max_length=10, choices=CPU_CHOICES)
    gpu = models.CharField(max_length=20, choices=GPU_CHOICES)
    ram = models.CharField(max_length=10, choices=RAM_CHOICES)
    storage = models.CharField(max_length=10, choices=STORAGE_CHOICES)
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.score}"
