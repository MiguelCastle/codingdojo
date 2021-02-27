from django.db import models
from django.contrib.auth.models import User


class Wallet(models.Model):
    balance = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.user, self.balance)

class Borrower(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='borrower'
    )
    reason = models.TextField(max_length=255)
    description = models.TextField(max_length=600)
    amount_needed = models.IntegerField()

    def __str__(self):
        return '%s %s %s %s' % (self.user, self.reason, self.description, self.amount_needed)

class Contract(models.Model):
    contract_lender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='contract_lender',
        blank=True,
        null=True
    )

    contract_borrower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='contract_borrower',
        blank=True,
        null=True
    )
    amount = models.IntegerField()
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.contract_lender