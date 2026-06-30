from django.db import models
from django.contrib.auth.models import User

class Prediction(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    gender = models.CharField(max_length=10)
    married = models.CharField(max_length=10)
    dependents = models.CharField(max_length=5)
    education = models.CharField(max_length=20)
    self_employed = models.CharField(max_length=10)

    applicant_income = models.FloatField()
    coapplicant_income = models.FloatField()
    loan_amount = models.FloatField()
    loan_amount_term = models.FloatField()

    credit_history = models.CharField(max_length=10)
    property_area = models.CharField(max_length=20)

    prediction = models.CharField(max_length=20)
    confidence = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.prediction}"