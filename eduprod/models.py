from django.db import models
from django.db import models

class ContinentQuestions(models.Model):
    CONTINENT_CHOICES = [
        ('Africa', 'Africa'),
        ('Asia', 'Asia'),
        ('Europe', 'Europe'),
        ('North America', 'North America'),
        ('South America', 'South America'),
        ('Oceania', 'Oceania'),
    ]

    question_text = models.CharField(max_length=200)
    answer_text = models.CharField(max_length=200)
    continent = models.CharField(max_length=50, choices=CONTINENT_CHOICES)

    def __str__(self):
        return f"{self.question_text} - {self.continent}"
    pass

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer_text = models.TextField()
    category = models.CharField(max_length=50, default='Europe')

    def __str__(self):
        return self.question_text