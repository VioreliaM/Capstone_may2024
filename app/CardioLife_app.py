#CardioLife App

#import libraries
import pandas as pd
import numpy as np
import streamlit as st
import pickle
import base64
import joblib
import shap
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
#for warning messages
from pretty_notification_box import notification_box
styles = {'material-icons':{'color': 'red'},
          'title': {'font-weight':'bold'},
          'notification-content-container': {'':''},
          'title-text-url-container': {'',''},
          'notification-text-link-close-container': {'',''},
          'external-link': {'',''},
          'close-button': {'',''}}

# Extract the model
model = joblib.load('/Users/vioreliamagari/Desktop/capstone_may2024/app/final_rf_model.pkl')

#Function to write the prediction: 
def cvd_prediction(input_df):

    prediction = model.predict(input_df)
    # Write the prediction result
    if prediction[0] == 1:
            notification_box(icon='warning', title='Warning', 
                             textDisplay='Your risk of having a cardiovascular disease in the future is HIGH!',
                             externalLink='',
                             url='', styles=None, key='foo')
    else:
            st.balloons()
            st.success('Your risk of having a cardiovascular disease is LOW!')

#Function to wrtite the reccomendations
def reccomendations(input_df):
    # Explain the model's predictions using SHAP
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(input_df)
    # Extract SHAP values for positive output
    shap_values_pos = shap_values[0][:, 1]  
    # Create DataFrames for SHAP values of positive output
    shap_values_df = pd.DataFrame(shap_values_pos.reshape(1, -1), columns=input_df.columns)
    
    # Display the reccomendations:
    #If Body Mass Index is high:
    #Calculate the number of calories the user should eat:
    def calculate_calories(input_df):
        if (input_df['active'].any() == 0).any():
            AMR = 1.2
        else:
            AMR = 1.375
        if (input_df['gender'] == 0).any():
            calories = ((655.1 + (9.563 * input_df['weight']) + 
                        (1.850 * input_df['height']) - 
                        (4.676 * (input_df['age'])/365 )) * AMR).astype(int) 
        else:
            calories = ((66.47 + (13.75 * input_df['weight']) + 
                        (5.003 * input_df['height']) - 
                        (6.755 * (input_df['age'])/365 )) * AMR).astype(int)
        return calories.astype(str)
    calories = calculate_calories(input_df)
    if (shap_values_df['bmi'] > 0.01).any() :
        st.warning("Your Body Mass Index is high! ")
        st.write('You should exercise minimum 20 minutes per day x 3 times per week!') 
        st.write('You should eat: ', calories[0], ' amount of calories per day!')
 
    #If blood pressure is high:
    if (shap_values_df['ap_hi'] > 0.03).any() | (shap_values_df['ap_lo'] > 0.03).any():
        st.warning('Please make an appoitment with your family doctor or with a cardiologist, to manage your high blood pressure and to take medications!')
    
    # If cholesterol is high:
    if (shap_values_df['cholesterol_3']> 0.03).any() :
        st.warning('Please make an appoitment with your family doctor, to manage your high cholesterol and to take medications!')
    
#######################################################################################################################################
#MAIN function of the app:
def main():
    #st.title('CardioLife')
    # Make a sidebar with logo and description of the app
    st.markdown("""
    <style>
        [data-testid=stSidebar] {
            background-color: #ff000050;
        }
    </style>
    """, unsafe_allow_html=True)
    with st.sidebar:
        st.image("/Users/vioreliamagari/Desktop/capstone_may2024/images/logoCardioLife.png") 
        st.markdown("<h1 style='text-align: center;'>A predictive model that forecasts the probability of having cardiovascular disease (CVD)</h1>", unsafe_allow_html=True)
        st.markdown("<h3> Welcome to CardioLife app!</h3>", unsafe_allow_html=True)
        st.write(''' This app will predict the likelihood of having a CVD in the future, based on your personal data!
                Also, if you have certain risks that will lead to having a CVD, the app will write recommendations on how you can minimize those risks!
                 ''')

    #Header
    st.markdown("<h2 style='text-align: center;'> Enter your data, then press the button: Predict! </h2>", unsafe_allow_html=True)
    #Getting input data from the user
    age = st.date_input("Select your birthday: ", key='birthday')
    gender = st.radio('Select gender: ', ['F', 'M'], key='gender')
    weight = st.slider("Select weight (kilograms)", 40, 200, 70, key='weight')
    height = st.slider("Select height (cm)", 120, 220, 170, key='height')
    ap_hi = st.slider("Choose systolic blood pressure: ", 50, 200, 120, key='systbp')
    ap_lo = st.slider("Choose diastolic blood pressure: ", 20, 160, 80, key='diastbp')
    cholesterol = st.selectbox("Select the level of the cholesterol: ", ["Normal","Above normal","Well above normal"], key="cholesterol")
    gluc = st.selectbox("Select the level of the glucose: ", ["Normal","Above normal","Well above normal"], key="glucose")
    smoke = st.radio("Are you smoking? ", ["No","Yes"], key="smoking")
    alco = st.radio("Are you drinking alcohol? ", ["No","Yes"], key="drinking")
    active = st.radio("Do you have an active lifesyle?", ["No","Yes"], key="active")

    #Data pre-processing for modelling 
    #Create a dataframe with user's data
    user_df = pd.DataFrame({
            'age': [age],
            'gender': [gender],
            'height': [height],
            'weight': [weight],
            'ap_hi': [ap_hi],
            'ap_lo': [ap_lo],
            'cholesterol': [cholesterol],
            'gluc': [gluc],
            'smoke': [smoke],
            'alco': [alco],
            'active': [active] 
        })

    #Convert date into number of days
    user_df['age'] = pd.to_datetime(user_df['age'])
    current_date = pd.Timestamp.now().normalize()
    user_df['age'] = (current_date - user_df['age']).dt.days

    #Convert gender to a binary value
    def map_gender(value):
        if value == 'F':
            return 0
        else:
            return 1
    user_df['gender'] = user_df['gender'].apply(map_gender)
    
    #Convert from string to numeric
    user_df['weight'] = pd.to_numeric(user_df['weight'])
    user_df['height'] = pd.to_numeric(user_df['height'])
    user_df['ap_hi'] = pd.to_numeric(user_df['ap_hi'])
    user_df['ap_lo'] = pd.to_numeric(user_df['ap_lo'])
    #Calculate Body index mass column
    user_df['bmi'] = user_df['weight'] / ((user_df['height']/100) ** 2)

    #Map cholesterol column 
    def map_chgluc(value):
        if value == 'Normal':
            return 1
        elif value == 'Above normal':
            return 2
        else:
            return 3
    user_df['cholesterol'] = user_df['cholesterol'].apply(map_chgluc)

    #Map glucose column
    user_df['gluc'] = user_df['gluc'].apply(map_chgluc)

    #Map smoking, drinking and active
    def map_yesno(value):
        if value == 'No':
            return 0
        else:
            return 1
    user_df['smoke'] = user_df['smoke'].apply(map_yesno)
    user_df['alco'] = user_df['alco'].apply(map_yesno)
    user_df['active'] = user_df['active'].apply(map_yesno)

    # Transform the cholesterol and glucose column, like onehotencoder for modelling
    cholesterol_dummies = pd.get_dummies(user_df['cholesterol'], prefix='cholesterol').astype(int)
    glucose_dummies = pd.get_dummies(user_df['gluc'], prefix='gluc').astype(int)

    #Make dummies columns for other blood test results, as we have them in our model
    dummies_chol = ['cholesterol_1', 'cholesterol_2', 'cholesterol_3']
    for col in dummies_chol:
        if col not in cholesterol_dummies.columns:
            cholesterol_dummies[col] = 0
    dummies_gluc = ['gluc_1', 'gluc_2', 'gluc_3']
    for col in dummies_gluc:
        if col not in glucose_dummies.columns:
            glucose_dummies[col] = 0

    #Place the columns in the right order
    order_ch = ['cholesterol_1', 'cholesterol_2', 'cholesterol_3'] 
    order_gl = ['gluc_1', 'gluc_2', 'gluc_3']

    # Reorder columns 
    cholesterol_dummies = cholesterol_dummies[order_ch]
    glucose_dummies = glucose_dummies[order_gl]

    # Concatenate the dummy columns back to the original DataFrame
    user_df = pd.concat([user_df, cholesterol_dummies, glucose_dummies], axis=1)
    # Drop the original columns
    user_df.drop(['cholesterol', 'gluc'], axis=1, inplace=True)

    #Creating a button for predictions: 
    #cardio = ''
    if st.button('Predict'):
        cardio = cvd_prediction(user_df)
        #reccomen = ''
        reccomen = reccomendations(user_df)
    

if __name__ == '__main__':
    main()