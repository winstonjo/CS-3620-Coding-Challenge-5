from django.db import models

# Create your models here.


class Hobby(models.Model):

    def __str__(self):
        return self.hobby_name

    hobby_name = models.CharField(max_length=200)
    hobby_dec = models.CharField(max_length=200)
    hobby_image = models.CharField(max_length=500, default='https://www.google.com/imgres?imgurl=http%3A%2F%2Fwww.campustimes.org%2Fwp-content%2Fuploads%2F2022%2F09%2FCatherine_xie_hobbies_CT-800x560-c-default.png&tbnid=TE6WuWLR3XNkVM&vet=12ahUKEwjr0dDtlruEAxXkxskDHQb2AekQMygBegQIARBP..i&imgrefurl=https%3A%2F%2Fwww.campustimes.org%2F2022%2F09%2F13%2Fthe-mysterious-case-of-the-disappearing-hobbies%2F&docid=7Gkpi1zFZLf8kM&w=800&h=560&q=hobbies%20default%20image&ved=2ahUKEwjr0dDtlruEAxXkxskDHQb2AekQMygBegQIARBP')


class Portfolio(models.Model):

    def __str__(self):
        return self.portfolio_name

    portfolio_name = models.CharField(max_length=200)
    portfolio_dec = models.CharField(max_length=200)
    portfolio_image = models.CharField(max_length=500, default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fdepositphotos.com%2Fphotos%2Fportfolio.html&psig=AOvVaw0sFFGGt_i295EAAF6M75Jo&ust=1708559773494000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCJCO8riPu4QDFQAAAAAdAAAAABAE')