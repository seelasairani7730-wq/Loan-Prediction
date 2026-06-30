from django.shortcuts import render
from .ai_model import predict_loan
from .models import Prediction
from django.db.models import Avg
from django.shortcuts import redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")


@login_required
def predict(request):

    if request.method == "POST":

        result, confidence = predict_loan(request.POST)

        # Save prediction to database
        Prediction.objects.create(

            user=request.user,

            gender=request.POST["gender"],
            married=request.POST["married"],
            dependents=request.POST["dependents"],
            education=request.POST["education"],
            self_employed=request.POST["self_employed"],
            applicant_income=request.POST["applicant_income"],
            coapplicant_income=request.POST["coapplicant_income"],
            loan_amount=request.POST["loan_amount"],
            loan_amount_term=request.POST["loan_amount_term"],
            credit_history=request.POST["credit_history"],
            property_area=request.POST["property_area"],

            prediction=result,
            confidence=confidence

        )

        return render(request, "result.html", {

            "result": result,
            "confidence": confidence

        })

    return render(request, "predict.html")

@login_required
def history(request):

    predictions = Prediction.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(request, "history.html", {
        "predictions": predictions
    })


@login_required
def dashboard(request):

    predictions = Prediction.objects.filter(user=request.user)

    total = predictions.count()

    approved = predictions.filter(
        prediction="Approved"
    ).count()

    rejected = predictions.filter(
        prediction="Rejected"
    ).count()

    average = predictions.aggregate(
        Avg("confidence")
    )["confidence__avg"]

    if average is None:
        average = 0

    return render(request, "dashboard.html", {

        "total": total,

        "approved": approved,

        "rejected": rejected,

        "average": round(average, 2)

    })

def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")

        else:
            print(form.errors)   # <-- Add this

    else:

        form = RegisterForm()

    return render(request, "register.html", {
        "form": form
    })

def login_user(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("home")

        else:

            return render(request, "login.html", {
                "error": "Invalid Username or Password"
            })

    return render(request, "login.html")


def logout_user(request):

    logout(request)

    return redirect("home")