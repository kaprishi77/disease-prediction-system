import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Sidebar navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        try:
            input_data = [float(Pregnancies), float(Glucose), float(BloodPressure),
                          float(SkinThickness), float(Insulin), float(BMI),
                          float(DiabetesPedigreeFunction), float(Age)]
            diab_prediction = diabetes_model.predict([input_data])
            diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        except:
            diab_diagnosis = 'Invalid input. Please enter numeric values.'
    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex_input = st.selectbox('Sex', ['Male', 'Female'])
        sex = 1 if sex_input == 'Male' else 0
    with col3:
        cp_input = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
        cp = ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'].index(cp_input)
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl')
    with col3:
        fbs_input = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['Yes', 'No'])
        fbs = 1 if fbs_input == 'Yes' else 0
    with col1:
        restecg_input = st.selectbox('Resting ECG Results', ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'])
        restecg = ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'].index(restecg_input)
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang_input = st.selectbox('Exercise Induced Angina', ['Yes', 'No'])
        exang = 1 if exang_input == 'Yes' else 0
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope_input = st.selectbox('Slope of Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
        slope = ['Upsloping', 'Flat', 'Downsloping'].index(slope_input)
    with col3:
        ca = st.text_input('Number of Major Vessels (0–3) colored by fluoroscopy')
    with col1:
        thal_input = st.selectbox('Thalassemia Type', ['Normal', 'Fixed Defect', 'Reversible Defect'])
        thal = ['Normal', 'Fixed Defect', 'Reversible Defect'].index(thal_input)

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        try:
            input_data = [float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs),
                          float(restecg), float(thalach), float(exang), float(oldpeak), float(slope),
                          float(ca), float(thal)]
            heart_prediction = heart_disease_model.predict([input_data])
            heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'
        except:
            heart_diagnosis = 'Invalid input. Please enter numeric values.'
    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    fields = ['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 'MDVP:RAP',
              'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5',
              'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE']
    inputs = []
    cols = st.columns(5)
    for i, field in enumerate(fields):
        with cols[i % 5]:
            inputs.append(st.text_input(field))
    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        try:
            input_data = [float(i) for i in inputs]
            parkinsons_prediction = parkinsons_model.predict([input_data])
            parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        except:
            parkinsons_diagnosis = 'Invalid input. Please enter numeric values.'
    st.success(parkinsons_diagnosis)
