import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


# Create your models here.
class Question(models.Model):
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    
    def __str__(self):
        return self.description
    
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - \
            datetime.timedelta(days=1)
        

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.description
    