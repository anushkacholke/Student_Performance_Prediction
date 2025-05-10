📊 Student Performance Prediction
This project predicts student academic performance based on various demographic, educational, and behavioral features using a machine learning model. It includes a Flask web interface for input and prediction.


🚀 Features

Trained ML model (Random Forest Classifier)

Web interface using Flask

Data preprocessing: label encoding, scaling

Evaluation: accuracy, precision, recall, F1 score, confusion matrix

Deployment-ready structure


🧠 Machine Learning

Model Used: Random Forest Classifier (n_estimators=100)

Evaluation Metrics:

Accuracy

Precision

Recall

F1 Score

Confusion Matrix (visualized)


📁 Project Structure

student-performance-prediction/

│

├── app.py                  # Flask app

├── student_performance_model.pkl

├── scaler.pkl

├── label_encoders.pkl

├── feature_order.pkl

├── templates/

│   ├── index.html

│   └── result.html

├── static/

│   └── style.css 

├── Notebook

    └── ResearchInformation3.csv 
    
    └── student_prediction_system.ipynb

    
🧪 Technologies Used

Python

Pandas, NumPy

scikit-learn

Flask

HTML/CSS

Seaborn/Matplotlib (for visualization)

📝 Dataset

The dataset includes student details such as:

Gender, Department, Family Income

Academic scores (HSC, SSC)

Internet/computer access

Job status, English proficiency

Semester performance

📷 Screenshots
![image](https://github.com/user-attachments/assets/61c1e172-4cda-477f-999a-9b7a2287938c)
![image](https://github.com/user-attachments/assets/dccead90-7850-4306-854d-99928b5ffede)
Confussion matrix: ![image](https://github.com/user-attachments/assets/25560eaa-908c-499d-be7e-e726073026f5)

✅ Results

Model Accuracy: 72 %

Confusion matrix showed strong classification in most categories

Supports prediction based on real-world student input

🙋‍♂️ Author

Miss. Anushka Rahul Cholke

LinkedIn Profile: https://in.linkedin.com/in/anushka-cholke-672723293

Portfolio: https://anushka-my-portfolio.netlify.app/


