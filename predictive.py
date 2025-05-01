import joblib
import pandas as pd

# Load model pipeline yang sudah dilatih
model = joblib.load("Hasil Predicted.pkl")

# Contoh data baru (ganti dengan data HR asli dalam DataFrame)
data_baru = pd.DataFrame({
    'Age': [28],
    'Department': ['Research & Development'],
    'DistanceFromHome': [5],
    'Education': [3],
    'Gender': ['Male'],
    'JobRole': ['Research Scientist'],
    'MonthlyIncome': [5000],
    'NumCompaniesWorked': [1],
    'TotalWorkingYears': [6],
    'YearsAtCompany': [4],
})

# Prediksi
prediksi = model.predict(data_baru)
print("Hasil Prediksi:", prediksi)

# Menyimpan hasil
data_baru['Prediction'] = prediksi
data_baru.to_csv('hasil_prediksi_hr.csv', index=False)
