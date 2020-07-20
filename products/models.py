from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=255)
    url = models.TextField()
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField('images/')
    icon = models.ImageField('images/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return self.body[:100]
    
    def pub_date_pretty(self):
       return self.pub_date.strftime('%b %e %Y') 

    def __str__(self):
        return self.title