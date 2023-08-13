# Import Libraries
import streamlit as st
st.set_page_config(layout="wide", initial_sidebar_state="expanded", )
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit.components.v1 as components
import requests

# Dataset
url = "Loan.xlsx"

# Prediction Function connected to the FAST API
def get_predictions(CHK_ACCT, DURATION,	HISTORY, SAV_ACCT, EMPLOYMENT, REAL_ESTATE,	PROP_UNKN_NONE,	AGE, OTHER_INSTALL,	OWN_RES):
    url = 'https://loan-credit-scorecard-8730a72d721d.herokuapp.com//predict?CHK_ACCT={CHK_ACCT}&DURATION={DURATION}&HISTORY={HISTORY}&SAV_ACCT={SAV_ACCT}&EMPLOYMENT={EMPLOYMENT}&REAL_ESTATE={REAL_ESTATE}&PROP_UNKN_NONE={PROP_UNKN_NONE}&AGE={AGE}&OTHER_INSTALL={OTHER_INSTALL}&OWN_RES={OWN_RES}' \
        .format(CHK_ACCT=CHK_ACCT, DURATION=DURATION, HISTORY=HISTORY, SAV_ACCT=SAV_ACCT, EMPLOYMENT=EMPLOYMENT, REAL_ESTATE=REAL_ESTATE, PROP_UNKN_NONE=PROP_UNKN_NONE, AGE=AGE, OTHER_INSTALL=OTHER_INSTALL, OWN_RES=OWN_RES)
    response = requests.post(url)
    json_response = response.json()
    score=json_response['prediction']
    return score

# Side Bar
# st.sidebar.image('photos/logo.png')
st.sidebar.header("Loan Credit Score")
menu = ['Get Score','Exploratory Data Analysis','About']
selection = st.sidebar.selectbox("", menu)

st.sidebar.write('Financial institutions find it crucial to forecast the likelihood of loan repayment for new clients in order to anticipate the potential for loan default and mitigate the expenses associated with borrowers who may not fulfill their repayment obligations.')

# Get Price Functionality
if selection == 'Get Score':
    st.columns(2)    
    # st.image('photos/phones.jpg')
    st.title('Enter customer details')
    # st.image('photos/specs.png')
    CHK_ACCT = st.number_input('Customer account status.', min_value=0 , max_value=3)
    st.write('0 (account status with < 0 DM), 1 (account status with 0 < ...< 200 DM), 2 (account status with => 200 DM), 3 (no checking account)') 
    DURATION = st.number_input('Customer duration of credit in months.')
    HISTORY = st.number_input('Customer credit history.', min_value=0 , max_value=4)
    st.write('0 (no credits taken), 1 (all credits at this bank paid back duly), 2 (existing credits paid back duly till now), 3 (delay in paying off in the past), 4 (critical account)')
    SAV_ACCT = st.number_input('Customer average balance in savings account.', min_value=0 , max_value=4)
    st.write('0 (acc avg bal < 100 DM), 1 (acc avg bal 100<= ... <  500 DM), 2 (acc avg bal 500<= ... < 1000 DM), 3 (acc avg bal =>1000 DM), 4 (unknown/ no savings account)')
    EMPLOYMENT = st.number_input('Customer employment period.', min_value=0 , max_value=4)
    st.write('0 (unemployed), 1 (< 1 yr), 2 (1 <= ... < 4 yrs), 3 (4 <=... < 7 yrs), 4 (>= 7 yrs)')
    REAL_ESTATE = st.number_input('Customer owns real estate.', min_value=0 , max_value=1)
    st.write('0 - No, 1 - Yes')
    PROP_UNKN_NONE = st.number_input('Customer owns no property (or unknown).', min_value=0 , max_value=1)
    st.write('0 - No, 1 - Yes')
    AGE = st.number_input('Customers age in years.')
    OTHER_INSTALL = st.number_input('Customer has other installment plan credit.', min_value=0 , max_value=1)
    st.write('0 - No, 1 - Yes')
    OWN_RES = st.number_input('Customer owns residence.', min_value=0 , max_value=1)
    st.write('0 - No, 1 - Yes')
    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = get_predictions(CHK_ACCT=CHK_ACCT, DURATION=DURATION, HISTORY=HISTORY, SAV_ACCT=SAV_ACCT, EMPLOYMENT=EMPLOYMENT, REAL_ESTATE=REAL_ESTATE, PROP_UNKN_NONE=PROP_UNKN_NONE, AGE=AGE, OTHER_INSTALL=OTHER_INSTALL, OWN_RES=OWN_RES)
        st.success(f'Credit Rating: {result}')
        st.write('0 - No, 1 - Yes')
        # st.image('photos/phoness.jpg')


        
# Exploratory Data Analysis Functionality
if selection == 'Exploratory Data Analysis':    
    df = pd.read_excel(url)
    st.markdown('Display data')
    st.table(df.head())

    # Total Amount Disbursed
    # Calculate the sum of 'AMOUNT' column
    total_amount = df['AMOUNT'].sum()
    # Print the sum with commas as thousands separators
    st.write(total_amount)

    # Percentage of Good and Bad Creditors
    # Calculate value counts
    response_counts = df['RESPONSE'].value_counts()
    # Create the pie chart using Plotly Express
    fig = px.pie(response_counts, names=response_counts.index, values=response_counts.values, title='PIE CHART SHOWING GOOD & BAD DEBTORS')
    # Display the pie chart using Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # Amount Disbursed in relation to Response
    response_amount_sum = df.groupby('RESPONSE')['AMOUNT'].sum()
    # Print the total amount for each response with commas
    print(response_amount_sum.apply('{:,}'.format))
    st.write('{response_amount_sum}')


# adding html  Template

footer_temp = """
	 <!-- CSS  -->
	  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
	  <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	  <link href="static/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	   <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
	 <footer class="page-footer grey darken-4">
	    <div class="container" id="aboutapp">
	      <div class="row">
	        <div class="col l6 s12">
	          <h5 class="white-text">Loan Credit Score</h5>
	          <p class="grey-text text-lighten-4">Streamlit Practical.</p>
	        </div>
	   <div class="col l3 s12">
	          <h5 class="white-text">Connect With Me</h5>
	          <ul>
	          <a href="www.linkedin.com/in/lewis-kimtai" target="_blank" class="white-text">
	            <i class="fab fa-linkedin fa-4x"></i>
	          </a>
	           <a href="https://github.com/lewiskimtai" target="_blank" class="white-text">
	            <i class="fab fa-github-square fa-4x"></i>
	          </a>
	          </ul>
	        </div>
	      </div>
	    </div>
	    <div class="footer-copyright">
	      <div class="container">
	      Made by <a class="white-text text-lighten-3" https://lewiskimtai.github.io/">Kimtai Lewis</a><br/>
	      <a class="white-text text-lighten-3" href="https://lewiskimtai.github.io/"></a>
	      </div>
	    </div>
	  </footer>
	"""


# About Functionality
if selection == 'About':
    st.subheader("About App")
    st.text('''
                Welcome to our Credit Score App, your reliable partner in assessing and understanding your financial health. 
            Our user-friendly platform empowers you with insights into your creditworthiness, offering a comprehensive analysis 
            of your credit history and providing valuable guidance to help you make informed financial decisions. 
            Whether you're planning for a major purchase, seeking better loan terms, or simply aiming to enhance your financial well-being, 
            our Credit Score App is here to support you on your journey towards a secure and prosperous future.
            ''')
    components.html(footer_temp, height=500)