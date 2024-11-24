import joblib

model = joblib.load('gdp_predictor_model.joblib')
print("Please enter integer year input to predict the simple gdp")
inp=int(input("'2034' in this format>>>]"))


predicted_gdp = model.predict([[inp]])
print(f"Predicted GDP for 2025: {predicted_gdp[0]:,.2f}")