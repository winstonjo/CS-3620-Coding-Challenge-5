from django.db import models

# Create your models here.

#copy image address

class Hobby(models.Model):

    def __str__(self):
        return self.hobby_name

    hobby_name = models.CharField(max_length=200)
    hobby_dec = models.CharField(max_length=200)
    hobby_image = models.CharField(max_length=500, default='https://www.google.com/imgres?imgurl=https%3A%2F%2Ffjwp.s3.amazonaws.com%2Fblog%2Fwp-content%2Fuploads%2F2020%2F02%2F29113959%2Fhobby-money.png&tbnid=0COPFv_BvKsdXM&vet=12ahUKEwjikaKEiruEAxWqh-4BHdb0BHgQMygCegQIARB5..i&imgrefurl=https%3A%2F%2Fwww.flexjobs.com%2Fblog%2Fpost%2Fhobbies-turn-into-good-side-job%2F&docid=N42HQBTL9mxTaM&w=1600&h=800&q=hobbies%20image&ved=2ahUKEwjikaKEiruEAxWqh-4BHdb0BHgQMygCegQIARB5')


class Portfolio(models.Model):

    def __str__(self):
        return self.portfolio_name

    portfolio_name = models.CharField(max_length=200)
    portfolio_dec = models.CharField(max_length=200)