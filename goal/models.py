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
    def __str__(self):
        return self.description

