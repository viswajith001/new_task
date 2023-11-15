from django.db import models
from user_interface.models import MyUser 

STATUS_CHOICES = (  
    ('inprogress', 'In Progress'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled'),
)

class MyTask(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)  

    def __str__(self):
        return self.title
