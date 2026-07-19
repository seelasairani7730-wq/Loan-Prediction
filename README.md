# 🏦 AI Loan Eligibility Prediction System

An AI-powered web application built using **Django** and **Machine Learning** to predict whether a loan application is likely to be approved based on applicant details.

---

## 📌 Project Overview

This project uses a trained Machine Learning model to analyze applicant information and predict loan eligibility. The application also provides prediction confidence, stores prediction history, and includes user authentication with a dashboard.

---

## 🚀 Features

* 🤖 AI-based loan eligibility prediction
* 📊 Prediction confidence score
* 👤 User Registration & Login
* 🔒 Secure Authentication
* 📜 Prediction History
* 📈 Dashboard with Analytics
* 💾 Database Storage
* 📱 Responsive User Interface
* ⚡ Fast Prediction Results

---

## 🛠 Tech Stack

### Backend

* Python
* Django

### Machine Learning

* TensorFlow / Keras
* Scikit-learn
* NumPy
* Pandas

### Frontend

* HTML5
* CSS3
* Bootstrap 5

### Database

* SQLite

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```
Loan-Prediction/
│
├── predictor/
├── config/
├── templates/
├── static/
├── media/
├── loan_model.keras
├── scaler.pkl
├── manage.py
├── requirements.txt
├── build.sh
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/seelasairani7730-wq/Loan-Prediction.git
cd Loan-Prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open your browser:

```
http://127.0.0.1:8000/
```

---

## 📊 Input Features

The prediction model uses the following applicant details:

* Gender
* Marital Status
* Number of Dependents
* Education
* Self Employed
* Applicant Income
* Co-applicant Income
* Loan Amount
* Loan Amount Term
* Credit History
* Property Area

---

## 🎯 Prediction Output

The application predicts:

* ✅ Loan Approved
* ❌ Loan Rejected

Along with a confidence score.

---

## 📈 Future Improvements

* Deploy using Docker
* MySQL/PostgreSQL Integration
* Admin Analytics Panel
* Email Notifications
* REST API
* Explainable AI (Feature Importance)
* Improved ML Model
* Cloud Deployment

---

## 👨‍💻 Author

**Seela SaiRani**

Passionate about Artificial Intelligence, Machine Learning, Full-Stack Development, and solving real-world problems through technology.

---

## ⭐ If you like this project

Please consider giving this repository a **Star ⭐**.
