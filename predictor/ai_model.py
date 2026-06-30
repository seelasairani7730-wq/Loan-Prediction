import os
import joblib
import numpy as np
from tensorflow.keras.models import load_model

# ======================================================
# Load Model & Scaler
# ======================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "ml_model", "loan_prediction_model.keras")

print("BASE_DIR:", BASE_DIR)
print("MODEL_PATH:", MODEL_PATH)
print("Exists:", os.path.exists(MODEL_PATH))

SCALER_PATH = os.path.join(BASE_DIR, "ml_model", "scaler.pkl")

model = load_model(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

print("✅ Model Loaded Successfully")
print("✅ Scaler Loaded Successfully")


# ======================================================
# Preprocess Input Data
# ======================================================

def preprocess(data):

    gender = 0 if data["gender"] == "Male" else 1

    married = 1 if data["married"] == "Yes" else 0

    dependents = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3+": 3
    }[data["dependents"]]

    education = 1 if data["education"] == "Graduate" else 0

    self_employed = 1 if data["self_employed"] == "Yes" else 0

    applicant_income = float(data["applicant_income"])

    coapplicant_income = float(data["coapplicant_income"])

    loan_amount = float(data["loan_amount"])

    loan_amount_term = float(data["loan_amount_term"])

    credit_history = 1 if data["credit_history"] == "Good" else 0

    property_area = {
        "Rural": 0,
        "Semiurban": 1,
        "Urban": 2
    }[data["property_area"]]

    # Create feature array
    features = np.array([[
        gender,
        married,
        dependents,
        education,
        self_employed,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_amount_term,
        credit_history,
        property_area
    ]], dtype=np.float32)

    # ============================================
    # Scale only numerical features
    # Columns:
    # 5 -> ApplicantIncome
    # 6 -> CoapplicantIncome
    # 7 -> LoanAmount
    # 8 -> Loan_Amount_Term
    # ============================================

    features[:, 5:9] = scaler.transform(features[:, 5:9])

    return features


# ======================================================
# Prediction Function
# ======================================================

def predict_loan(data):

    input_data = preprocess(data)

    # Debugging
    print("\n========== INPUT ==========")
    print(input_data)

    prediction = model.predict(input_data, verbose=0)
    print("Raw Prdection:", prediction)

    probability = float(prediction[0][0])

    print("Raw Probability:", probability)

    if probability >= 0.5:
        result = "Approved"
        confidence = probability * 100
    else:
        result = "Rejected"
        confidence = (1 - probability) * 100

    print("Prediction:", result)
    print("Confidence:", round(confidence, 2), "%")

    return result, round(confidence, 2)