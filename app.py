import os
import pickle
import streamlit as st  # type: ignore
from streamlit_option_menu import option_menu # type: ignore

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Doctor Consultation',
                            'Emergency Alert'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
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


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            #diab_diagnosis = 'You are diagonsed with diabetes\n \n '
            st.markdown('<p style="color:red; border-radius: 25px">                       <b>&nbsp;&nbsp;&nbsp;&nbsp;You are diagonsed with diabetes<b><br>                                                                                        &nbsp;&nbsp;&nbsp;&nbsp;Preventive measures:  <br>                                                                               --> Healthy Eaten<br>                                                                                                                   --> Regular Physical Activities<br>                                                                                                          --> Avoid Sugary Beverages<br>                                                                                                          --> Regular Health Checkup<br>                                                                                                                             --> Manage Stress</p>', unsafe_allow_html=True)
        else:
            st.success('You are not diagonsed with diabetes')

    #st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            st.markdown('<p style="color:red; border-radius: 25px">                        <b>&nbsp;&nbsp;&nbsp;&nbsp;You are diagnosed with heart disease.<b><br>                                                                                        &nbsp;&nbsp;&nbsp;&nbsp;Preventive measures: <br>                                                                               &nbsp;&nbsp;&nbsp;&nbsp;--> Regular Exercise<br>                                                                                                                      &nbsp;&nbsp;&nbsp;&nbsp;--> Maintain a healthy weight<br>                                                                                                         &nbsp;&nbsp;&nbsp;&nbsp;--> Manage Stress<br>                                                                                                                             &nbsp;&nbsp;&nbsp;&nbsp;--> Get Enough Sleep</p>', unsafe_allow_html=True)
        else:
            st.success('The person does not have any heart disease')

    #st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            #parkinsons_diagnosis = "You are diagonsed with Parkinson's disease. Please take these preventive measures.<br> --> Regular exersice <br> --> Healthy Diet<br> --> Adequate Vitamin-D<br> --> Manage Stress"
            st.markdown('<p style="color:red; border-radius: 25px">                       <b>&nbsp;&nbsp;&nbsp;&nbsp;You are diagonsed with Parkinsons disease.<b><br>                                                                                        &nbsp;&nbsp;&nbsp;&nbsp;Please take these preventive measures:<br>                                                                                                     &nbsp;&nbsp;&nbsp;&nbsp;--> Regular exersice <br>                                                                                                        &nbsp;&nbsp;&nbsp;&nbsp;--> Healthy Diet<br>                                                                                                                       &nbsp;&nbsp;&nbsp;&nbsp;--> Adequate Vitamin-D<br>                                                                                                                   &nbsp;&nbsp;&nbsp;&nbsp;--> Manage Stress     </p>', unsafe_allow_html=True)
        else:
            st.success('You are not diagonsed with Parkinsons disease.')

    #st.success(parkinsons_diagnosis)

# Doctor's Consultation Group
if selected == 'Doctor Consultation':
    st.title('🩺 Doctor Consultation')

    # Doctor data as a list of dictionaries
    doctors = [
        {'Name': 'Dr Gautam Naik', 'Type': 'Cardiologist', 'Phone': '+91 8069305511', 'Experience': '12 Years', 'Hospital': 'NH-19, South East Delhi, New Delhi, 110076'},
        {'Name': 'Dr Amit Mittal', 'Type': 'Cardiologist', 'Phone': '+91 8062207719', 'Experience': '11 Years', 'Hospital': 'Apollo Hospitals Indraprastha, New Delhi'},
        {'Name': 'Dr Gaurav Gupta', 'Type': 'Diabetologist', 'Phone': '+91 08800737264', 'Experience': '8 Years', 'Hospital': 'Galaxy Royal Shoppe, Gaur City 2, Greater Noida, UP, 201009'},
        {'Name': 'Dr Harsh Bardhan', 'Type': 'Diabetologist', 'Phone': '+91 9917XXXXXX', 'Experience': '10 Years', 'Hospital': '112 City Plaza, Gaur City-1, Sector 4, Noida, UP, 201009'},
        {'Name': 'Dr Mohit Bhatt', 'Type': 'Neurology', 'Phone': '+91 8010994994', 'Experience': '38 Years', 'Hospital': 'Kokilaben Dhirubani Hospital, Andheri, Mumbai'},
        {'Name': 'Dr Debashis Bhattacharyya', 'Type': 'Neurology', 'Phone': '+91 8010994994', 'Experience': '22 Years', 'Hospital': 'Narayana Multispeciality Hospital, Howrah, Kolkata'},
        {'Name': 'Dr Ajay Nihalani', 'Type': 'Psychiatrist', 'Phone': '+91 08130491951', 'Experience': '12 Years', 'Hospital': 'Rajhans Plaza, Ahinsa Khand-I, Indirapuram, Ghaziabad, UP'},
        {'Name': 'Dr Kapil K. Singhal', 'Type': 'Neurologist', 'Phone': '+91 9087898765', 'Experience': '22 Years', 'Hospital': '135, Opposite Avantika Hospital, Niti Khand 2, Ghaziabad, UP'},
        {'Name': 'Dr (Lt Den) C.S. Narayanan', 'Type': 'Neurologist', 'Phone': '+91 8372553627', 'Experience': '12 Years', 'Hospital': 'Manipal Hospital, Ghaziabad'}
    ]

    # Display each doctor one by one in a vertical format
    for doc in doctors:
        st.subheader(doc['Name'])
        st.write(f"**Type:** {doc['Type']}")
        st.write(f"**Phone:** {doc['Phone']}")
        st.write(f"**Experience:** {doc['Experience']}")
        st.write(f"**Hospital:** {doc['Hospital']}")
        st.markdown("---")  # divider line between doctors

# # Emergency Alert
# if selected == 'Emergency Alert':
#     st.title('Emergency Alert')
#     col1, col2, col3, col4, col5 = st.columns(5)
    
#     # HTML with inline CSS
#     with col1:
#         st.markdown('<p style="color:red; font-size: 28px;"><b>Working on...</b></p>', unsafe_allow_html=True)
    
    # Emergency Alert
if selected == 'Emergency Alert':
    st.title('🚨 Emergency Alert System')

    st.info("This section helps you reach emergency services quickly. "
            "Use the buttons or call the helplines below in case of urgent medical needs.")

    # Columns for layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📞 Emergency Helpline Numbers")
        st.write("🚑 **National Ambulance Helpline:** 102 / 108")
        st.write("🚓 **Police Helpline:** 100")
        st.write("🔥 **Fire Service:** 101")
        st.write("🧑‍⚕️ **Medical Helpline:** +91 8010 999 111")
        st.write("💊 **Poison Control Center:** 1800-11-6117")

    with col2:
        st.subheader("🏥 Nearby Hospitals (Sample Data)")
        st.write("• AIIMS Hospital, New Delhi — +91 11 2658 8500")
        st.write("• Apollo Hospital, New Delhi — +91 11 2987 1000")
        st.write("• Fortis Hospital, Noida — +91 120 430 0222")
        st.write("• Max Super Specialty, Saket — +91 11 2651 5050")

    st.markdown("---")

    st.subheader("⚡ Quick Alert System")
    name = st.text_input("Enter Your Name")
    location = st.text_input("Enter Your Current Location / City")
    contact = st.text_input("Enter Your Contact Number")

    if st.button("🚨 Send Emergency Alert"):
        if name and location and contact:
            st.success(f"✅ Emergency Alert Sent!\n\n"
                       f"Name: {name}\n"
                       f"Location: {location}\n"
                       f"Contact: {contact}\n\n"
                       f"Authorities have been notified (demo message).")
        else:
            st.warning("⚠️ Please fill in all details before sending the alert.")
