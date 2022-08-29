import datetime
from xmlrpc.client import boolean 
from django.contrib import admin
from django.db import models
from django.utils import timezone

# Creating database layout here, which consists of two models/tables, 1. Questions,  2. Choices.
# Questions will obviously have choices, so people can select their choice against a question/poll. So, it means both tables will be related to each other

class Question(models.Model):                                                   # Extenting the base 'models' class, so it's methods can be inhereted in our 'Question' class
    question_text = models.CharField(max_length=200)                            # This also creates an id automatically, which auto-increments by default and will be used as a primary key
    pub_date = models.DateTimeField('date published')

    def __str__(self):                                                          # Using this so, only question text can be shown in the admin area, otherwise it shows the question objects, which looks weird
        return self.question_text

    @admin.display(
        boolean = True,
        ordering = 'pub_date',
        description = 'Published recently?',
    )
    def was_published_recently(self):                                           # Custom method to check if the question is published recenttly
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now 

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)           #Using the ForiegnKey here to link it to the Questions table, and on_delete so, if a question is deleted, all it's choices should also be deleted.
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
