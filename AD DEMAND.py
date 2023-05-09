

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('C:/Users/admin/Videos/AD DEMAND/addemand.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Ad demand prediction using ml',
                          
                          [ 'Home',
                            'Ad demand prediction',
                           'graph comparsion',
                            'result'
                            ],
                          default_index=0)

# Diabetes Prediction Page
if (selected == 'Home'):
    
    # page title
    st.title('Ad demand prediction using ml')

    st.image("rsm2.jpg")


    

    st.image("ram1.jpg")
    
  
    
# Diabetes Prediction Page
if (selected == 'Ad demand prediction'):
    
    # page title
    st.title('Ad demand  prediction ml')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        DailyTimeSpentonSite= st.text_input('DailyTimeSpentonSite')
        
    with col2:
        Age = st.text_input('Age ')
    
    with col3:
        AreaIncome  = st.text_input('AreaIncome')
    
    with col1:
        DailyInternetUsage	 = st.text_input('DailyInternetUsage')
    
    with col2:
        Male= st.text_input('Male')
    
    with col3:
        CityCodes	 = st.text_input('CityCodes	')
    
    with col1:
        CountryCodes		 = st.text_input('CountryCodes	')
    
    with col2:
        Month = st.text_input('Month')

    with col3:
        Hour = st.text_input('Hour')
    
    
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('start up Result'):
        diab_prediction = diabetes_model.predict([[DailyTimeSpentonSite, Age, AreaIncome,
        DailyInternetUsage, Male, CityCodes, CountryCodes, Month,
        Hour]])

        st.success('The output is {}'.format(diab_prediction ))
        
        
        
    

# Parkinson's Prediction Page
if (selected == "graph comparsion"):
    
    # page title
    st.title("graph comparsion")

    st.image("Capture.png")


    st.image("Capture1.png")

             
    st.image("Capture2.png")

   
    
    
# Parkinson's Prediction Page
if (selected == "result"):
    
    # page title
    st.title("result")

    st.image("Capture3.png")


    
    
    
   

if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")




