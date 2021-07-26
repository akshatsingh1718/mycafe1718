from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.utils.translation import gettext as _
import datetime


    
class Sale(models.Model):
    user = models.ForeignKey(User, verbose_name= _("User"), on_delete=models.CASCADE)
    timestamp = models.DateTimeField(_("Sale Time"), default=datetime.datetime.utcnow)
    amount = models.IntegerField(default=0)
    desc = models.TextField(_("Desctiption"), blank=True, null=True)
    PAYMENT_TYPES = [
        ('online', 'online'),
        ('cash', 'cash'),
    ]
    payment_type = models.CharField(max_length=30, choices=PAYMENT_TYPES)


    def __str__(self):
        return f"{self.user.first_name}  at {self.timestamp}"


class DailyStatement(models.Model):
    # auto incremet product_id whenever new object is created
    # it is primary key of product table and Django makes it
    # by its own
    opening = models.IntegerField(_("Opening Balance"), default=0)
    timestamp = models.DateField(_("Date") ,auto_now_add=True)
    total_amt = models.IntegerField(blank=False, null=False, default=0)
    statements = models.ManyToManyField(Sale, blank=True, null=True)

    def __str__(self):
        return f'{self.timestamp}'