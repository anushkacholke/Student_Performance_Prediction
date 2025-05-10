from flask import Flask, render_template, request 
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and preprocessing tools
model = joblib.load("student_performance_model.pkl")
label_encoders = joblib.load("label_encoders.pkl")
scaler = joblib.load("scaler.pkl")
feature_order = joblib.load("feature_order.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input from form
        input_data = {
            'Department': request.form['department'],
            'Gender': request.form['gender'],
            'HSC': float(request.form['hsc']),
            'SSC': float(request.form['ssc']),
            'Income': request.form['income'],
            'Hometown': request.form['hometown'],
            'Computer': int(request.form['computer']),
            'Preparation': request.form['preparation'],
            'Gaming': request.form['gaming'],
            'Attendance': request.form['attendance'],
            'Job': request.form['job'],
            'English': int(request.form['english']),
            'Extra': request.form['extra'],
            'Semester': request.form['semester']
        }

        # Create DataFrame
        df = pd.DataFrame([input_data])

        # Encode categorical values
        for col, le in label_encoders.items():
            if col in df.columns:
                if df[col][0] not in le.classes_:
                    df[col] = le.transform([le.classes_[0]])
                else:
                    df[col] = le.transform(df[col])

        # Ensure column order matches training
        df = df.reindex(columns=feature_order)

        # Scale numeric data
        df_scaled = scaler.transform(df)

        # Predict
        prediction = model.predict(df_scaled)[0]

        return render_template('result.html', prediction=prediction)

    except Exception as e:
        return render_template('result.html', prediction=f"⚠️ Oops! Something went wrong: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)