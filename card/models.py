from django.db import models

# Create your models here.

class Card(models.Model):
    cardid = models.TextField(verbose_name='cardID', primary_key=True)
    cardcode = models.TextField(verbose_name='cardCODE')
    owner = models.TextField(verbose_name='Owner', blank=True)
    name = models.TextField(verbose_name='Name Surname', blank=True)
    position = models.TextField(verbose_name='Position', blank=True)
    company = models.TextField(verbose_name='Company', blank=True)
    website = models.TextField(verbose_name='Web Site', blank=True)
    mail = models.EmailField(verbose_name='E-Mail', blank=True)
    gsm = models.TextField(verbose_name= 'GSM', blank=True)
    fax = models.TextField(verbose_name= 'Fax', blank=True)
    instagramacc = models.TextField(verbose_name='Instagram Account', blank=True)
    twitteracc = models.TextField(verbose_name='Twitter Account', blank=True)
    linkedinacc = models.TextField(verbose_name='LinkedIn Account Link', blank=True)
    profilepic = models.ImageField(verbose_name='Profile Pic', blank=True, upload_to='static/images')
    def __str__(self):
        return self.cardid
