from django.db import models

class Goal(models.Model):
    name = models.CharField(max_length = 200)
    year = models.IntegerField()
    def __str__(self):
        return self.name

class Entry(models.Model):
    entry_date = models.DateTimeField('date of entry')
    description = models.TextField()
    goal = models.ForeignKey(Goal)
    hours_worked = models.IntegerField()
    def __str__(self):
        return self.description

class User(models.Model):
    username = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)

    def is_authenticated(self):
        return false
    
    def is_active(self):
        return false
