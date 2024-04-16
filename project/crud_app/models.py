from django.db import models

class Review(models.Model):
    STARS = [('*','1 STAR'),('**','2 STAR'),('***','3 STAR'),('****','4 STAR'),('*****','5 STAR')]
    product = models.CharField(max_length=10,null=True)
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    email = models.EmailField()
    date = models.DateField()
    comments = models.CharField(max_length=30)
    stars = models.CharField(max_length=10,choices=STARS)