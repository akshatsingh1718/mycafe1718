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
        return f"{self.user.first_name}  at {self.timestamp} ({self.amount})"


class DailyStatement(models.Model):
    # auto incremet product_id whenever new object is created
    # it is primary key of product table and Django makes it
    # by its own
    opening = models.IntegerField(_("Opening Balance"), default=0)
    timestamp = models.DateField(_("Date"), unique= True)
    total_amt = models.IntegerField(blank=False, null=False, default=0)
    statements = models.ManyToManyField(Sale, blank=True, null=True)

    # @total_amt.setter
    # def set_total_amt(self, value):
    #     self.total_amt = value

    @property
    def total_amt(self):
        statements = self.statements.all()
        total_amt = 0
        for smt in statements:
            total_amt += smt.amount
        return total_amt

    @property
    def total_online_amt(self):
        statements = self.statements.all()
        total_online_amt = 0
        for smt in statements:
            if smt.payment_type == 'online':
                total_online_amt += smt.amount
        return total_online_amt

    @property
    def total_cash_amt(self):
        statements = self.statements.all()
        total_cash_amt = 0
        for smt in statements:
            if smt.payment_type == 'cash':
                total_cash_amt += smt.amount
        return total_cash_amt

    def __str__(self):
        return f'{self.opening} : {self.total_amt} : {self.timestamp}'