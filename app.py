import streamlit as st 
from streamlit_option_menu import option_menu
import pickle
import pandas as pd



with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Predection Page","Graphs and Charts","Contact us"]
    )


if selected == 'Predection Page':


    st.title('Air Quality Index Prediction')

    dt = pickle.load(open('dt.pkl','rb'))


    

    select_co = st.slider('CO AQI Value',min_value = 0,max_value = 70,step = 1,value = 35)
    
    select_ozone = st.slider('Ozone',min_value = 0,max_value = 222,step = 1,value = 111)
    
    select_no2 = st.slider('No2',min_value = 0,max_value = 94,step = 1,value = 47)
    
    select_pm= st.slider('Pm2.5',min_value = 0,max_value = 500,step = 1,value = 250)
    
    
    
            
        
        
    if st.button('Predict'):
        input_df = pd.DataFrame({'CO AQI Value':[select_co],
                                 'Ozone AQI Value':[select_ozone],
                                 'NO2 AQI Value':[select_no2],
                                'PM2.5 AQI Value':[select_pm]
                                })

        # #st.table(input_df)
        result = round(float(dt.predict(input_df)),3)
        #result_percentage = dt.predict_proba(input_df)
        
        st.title('Predicted Outcome')
        
        st.header('AQI Value')
        
        st.info(result)
        
        if 0 < result <= 50:
            category = 'Good'
            
        elif 50 < result <= 99:
            category = 'Moderate'
            
        elif 99 < result <= 149:
            category = 'Unhealthy for Sensitive Groups'
            
        elif 149 < result <= 200:
            category = 'Unhealthy'
            
        elif 200 < result <= 300:
            category = 'Very Unhealthy'
            
        else: 
            category = 'Hazardous'
            
        st.header('AQI Category')
        
        st.info(category)



    
if selected == 'Contact us':

    st.header(":mailbox: Get In Touch With Us!")


    contact_form = """
    <form action="https://formsubmit.co/sudhansu15gouda@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style.css")





# Good 7 50
# Moderate 51 99
# Unhealthy for Sensitive Groups 100 149
# Unhealthy 150 200
# Very Unhealthy 201 296
# Hazardous 301 500