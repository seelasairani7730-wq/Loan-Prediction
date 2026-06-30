from django.contrib import admin
from .models import Prediction


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "prediction",
        "confidence",
        "applicant_income",
        "loan_amount",
        "created_at"
    )

    list_filter = (
        "prediction",
        "created_at"
    )

    search_fields = (
        "user__username",
    )